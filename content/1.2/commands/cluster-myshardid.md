---
title: "CLUSTER MYSHARDID"
description: "Returns the ID of this node's shard: a master's own ID, or a replica's master's."
version: "1.2"
command: "CLUSTER MYSHARDID"
syntax: "CLUSTER MYSHARDID"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER MYSHARDID
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the ID of this node's shard: the master and its replicas, which hold the same slots. Use it to tell which nodes belong together, for example to group the nodes of [`CLUSTER NODES`](cluster-nodes.md) by shard.

In KiviDB the shard ID is the master's node ID: a master returns its own [`CLUSTER MYID`](cluster-myid.md), and a replica returns its master's. So it changes when a replica takes over: after a failover, both nodes of the shard return the new master's ID. In Redis a shard has an ID of its own, which master and replicas share and which stays the same across failovers.

## Reply

The shard ID, 40 hexadecimal characters, as a string.

## Errors

- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

On a master, then on its replica:

```
> CLUSTER MYID
"74cea35fa9a656f033023e9f6cb3d78ef2b1a95a"
> CLUSTER MYSHARDID
"74cea35fa9a656f033023e9f6cb3d78ef2b1a95a"
```

```
> CLUSTER MYID
"95dc5ee672adb953ccc7fe76c427f5083b7c9b4b"
> CLUSTER MYSHARDID
"74cea35fa9a656f033023e9f6cb3d78ef2b1a95a"
```

After [`CLUSTER FAILOVER`](cluster-failover.md) on the replica, both return `"95dc5ee672adb953ccc7fe76c427f5083b7c9b4b"`.
