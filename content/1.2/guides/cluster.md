---
title: "Cluster"
description: "Spread a KiviDB dataset over several servers: creating a cluster, how keys are placed and found, moving slots, and failover."
version: "1.2"
weight: 30
---

A cluster spreads the keyspace over several masters, each with replicas of its own. It holds more than one server can, takes writes on every master, and replaces a master that fails with one of its replicas, on its own.

KiviDB's cluster is Redis Cluster: the same 16384 slots, the same redirections, the same `CLUSTER` commands and bus protocol. Cluster clients and `redis-cli --cluster` work with it unchanged.

## How keys are placed

Every key is in one of 16384 slots, the CRC16 of the key modulo 16384, and every slot is owned by one master. [`CLUSTER KEYSLOT`](../commands/cluster-keyslot.md) gives a key's.

A command sent to a master that does not own its key's slot is answered with `MOVED slot host:port`: the master that does. A cluster client remembers which master owns which slots, from [`CLUSTER SLOTS`](../commands/cluster-slots.md) or [`CLUSTER SHARDS`](../commands/cluster-shards.md), and sends each command to the right one; `redis-cli -c` follows the redirections.

A command with several keys works only if they are in the same slot; otherwise it gets `CROSSSLOT`. A key with a `{...}` in it is placed by what is between the braces only, its hash tag, so keys that share one share a slot:

```
> CLUSTER KEYSLOT {user:1}:cart
(integer) 10778
> CLUSTER KEYSLOT {user:1}:orders
(integer) 10778
> MSET {user:1}:cart 3 {user:1}:orders 7
OK
> MSET a 1 b 2
(error) CROSSSLOT Keys in request don't hash to the same slot
```

A cluster node has one database, `0`: [`SELECT`](../commands/select.md) of any other is refused.

## Creating a cluster

Start each node with [`cluster-enabled yes`](../reference/configuration.md#cluster-enabled). The nodes must reach each other on the client port and on the bus port, the client port plus 10000.

A node that is to be reached from other machines needs a password, or it refuses them ([`protected-mode`](../reference/configuration.md#protected-mode)). Give every node the same [`requirepass`](../reference/configuration.md#requirepass) and [`masterauth`](../reference/configuration.md#masterauth), so that replicas can log in to their masters:

```
kividb --cluster-enabled yes --requirepass s3cret --masterauth s3cret
```

Then join them, and share the slots out, with `redis-cli` from Redis 7 or 8. Six nodes make three masters with a replica each:

```
redis-cli -a s3cret --cluster create \
  10.0.0.1:6380 10.0.0.2:6380 10.0.0.3:6380 \
  10.0.0.4:6380 10.0.0.5:6380 10.0.0.6:6380 \
  --cluster-replicas 1
```

```
redis-cli -a s3cret --cluster check 10.0.0.1:6380
...
[OK] All nodes agree about slots configuration.
>>> Check for open slots...
>>> Check slots coverage...
[OK] All 16384 slots covered.
```

By hand, the same is [`CLUSTER MEET`](../commands/cluster-meet.md) from one node to each other one, [`CLUSTER ADDSLOTSRANGE`](../commands/cluster-addslotsrange.md) on each master, and [`CLUSTER REPLICATE`](../commands/cluster-replicate.md) on each replica.

Each node keeps its ID, the other nodes, and who owns which slot in [`nodes.conf`](../reference/configuration.md#cluster-config-file), in its working directory, and finds the cluster again from it when it restarts. Keep that file with the node's data.

### Behind NAT, in containers, in Kubernetes

A node tells the others, and clients, the address they see it connect from. Where that is not the address to reach it at, set [`cluster-announce-ip`](../reference/configuration.md#cluster-announce-ip) (or [`cluster-announce-hostname`](../reference/configuration.md#cluster-announce-hostname) with [`cluster-preferred-endpoint-type hostname`](../reference/configuration.md#cluster-preferred-endpoint-type)), [`cluster-announce-port`](../reference/configuration.md#cluster-announce-port) and [`cluster-announce-bus-port`](../reference/configuration.md#cluster-announce-bus-port).

Where clients reach a node on another port than the other nodes do, a Kubernetes NodePort or a load balancer that maps ports, set [`cluster-announce-client-port`](../reference/configuration.md#cluster-announce-client-port): it is the port given to clients, in `MOVED`, `ASK` and `CLUSTER SLOTS`, while the nodes keep using the client port between themselves. It can be changed while the node runs.

### Securing the bus

Anything that can reach a node's bus port can join the cluster, as in Redis. Keep the bus on a private network, or give every node the same [`cluster-bus-secret`](../reference/configuration.md#cluster-bus-secret): a node then has to prove it knows the secret before anything it sends on the bus is read. [`cluster-bus-port-protected-mode yes`](../reference/configuration.md#cluster-bus-port-protected-mode) refuses to start a node without one. With TLS builds, [`tls-cluster`](../reference/configuration.md#tls-cluster) encrypts the bus and replication.

## Adding a master and moving slots

A new node joins with `redis-cli --cluster add-node`, and owns no slots until some are moved to it:

```
redis-cli -a s3cret --cluster add-node 10.0.0.7:6380 10.0.0.1:6380
redis-cli -a s3cret --cluster reshard 10.0.0.1:6380 \
  --cluster-from <source id> --cluster-to <new id> --cluster-slots 1000 --cluster-yes
```

There are two ways a slot moves, and `redis-cli` from Redis 8.4 on uses the first where the server has it, as KiviDB does:

- **Atomic slot migration**, [`CLUSTER MIGRATION IMPORT`](../commands/cluster-migration.md), sent to the node that is to receive the slots. The source sends a copy of the slots' keys and then the writes that arrive for them, pauses writes for a moment, and hands the slots over. Clients see no `ASK`, only a `MOVED` at the end, and no write is lost.
- **Key by key**, the classic way: [`CLUSTER SETSLOT`](../commands/cluster-setslot.md) `IMPORTING` and `MIGRATING`, [`MIGRATE`](../commands/migrate.md) of the keys in batches, then `SETSLOT ... NODE`. Meanwhile, a key that has moved is answered with `ASK`, and a client retries it on the new node after [`ASKING`](../commands/asking.md).

[`CLUSTER MIGRATION STATUS`](../commands/cluster-migration.md) shows how a migration is going, and how long writes were paused for it.

## Failover

A node that does not hear from another for [`cluster-node-timeout`](../reference/configuration.md#cluster-node-timeout) milliseconds (15 seconds by default) suspects it; when a majority of masters suspect a master, it is marked `fail`, and its replicas stand for election. The one that wins takes the master's slots, the clients are redirected to it, and the cluster is `ok` again. When the old master comes back, it finds its slots taken, and becomes a replica of the node that took them.

To move a master's role to its replica without a failure, for maintenance, send [`CLUSTER FAILOVER`](../commands/cluster-failover.md) to the replica: the master stops writes, the replica catches up, and they swap, without losing a write.

While a slot has no master that works, the cluster's state is `fail`, and every node refuses keyed commands with `CLUSTERDOWN`. With [`cluster-require-full-coverage no`](../reference/configuration.md#cluster-require-full-coverage), nodes go on serving the slots that do have one.

Replication in a cluster is what it is between standalone servers, asynchronous: a write a master acknowledged and had not yet sent to its replica is lost if the replica takes its place. See [Replication](replication.md).

The replicas stand in order of how up to date they are: the one that has the most of the master's writes stands first, and the others wait, so it is the one elected. A replica that had lost touch with its master for longer than [`cluster-replica-validity-factor`](../reference/configuration.md#cluster-replica-validity-factor) node timeouts does not stand at all, since its data may be old; `0` lets it. Before 1.2, replicas were not ranked, and one that was behind could win ([kividb#107](https://github.com/kividbio/kividb/issues/107)).

## Reading from replicas

A client can send reads to a master's replicas, after [`READONLY`](../commands/readonly.md) on the connection; writes are still redirected to the master. What a replica returns can be a little behind. Cluster clients have an option for it (`read_from_replicas`, `scaleReads`, `ReadFrom`).

## Removing a node

Move its slots away, with `reshard`, then `redis-cli --cluster del-node`, or [`CLUSTER FORGET`](../commands/cluster-forget.md) of its ID on every node within 60 seconds. A forgotten node keeps its own idea of the cluster: [`CLUSTER RESET`](../commands/cluster-reset.md) it before using it again.

## Known issues

- [`CLUSTER REPLICAS`](../commands/cluster-replicas.md) replies with one string, not an array of lines. Filed as [kividb#138](https://github.com/kividbio/kividb/issues/138).
- [`CLUSTER SLOT-STATS ORDERBY`](../commands/cluster-slot-stats.md) sorts ascending unless told `DESC`. Filed as [kividb#139](https://github.com/kividbio/kividb/issues/139).
