---
title: "CLUSTER FLUSHSLOTS"
description: "Gives up every slot this node owns: afterwards it owns none."
version: "1.2"
command: "CLUSTER FLUSHSLOTS"
syntax: "CLUSTER FLUSHSLOTS"
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
CLUSTER FLUSHSLOTS
```

**Available since:** 1.1.0
<!-- generated: end -->
Gives up every slot this node owns: afterwards it owns none. The other masters' slots stay as they are. Use it on a node being rebuilt by hand, before [`CLUSTER ADDSLOTSRANGE`](cluster-addslotsrange.md) gives it a new set.

As in Redis, the node must hold no keys: while it does, it is refused with `ERR DB must be empty to perform CLUSTER FLUSHSLOTS.`. Empty it first, with [`FLUSHALL`](flushall.md), or move its slots with their keys to another master.

Both are since 1.2.1. In 1.2.0 it cleared every slot in this node's view, the other masters' too, so that the node went to `cluster_state:fail` until their heartbeats brought them back, and it kept the node's keys without serving them.

Only this node's view changes: the other nodes still send clients to it for its old slots, and it answers them with `CLUSTERDOWN Hash slot n is not served`. To move a master's slots to another master with their keys, reshard instead, as in [Adding a master and moving slots](../guides/cluster.md#adding-a-master-and-moving-slots).

## Reply

`OK`, `ERR DB must be empty to perform CLUSTER FLUSHSLOTS.` while the node holds keys, or `ERR This instance has cluster support disabled` on a server that is not a cluster node.

## Examples

On the master of slots 10923 to 16383, in a cluster of three:

```
> SET foo bar
OK
> CLUSTER FLUSHSLOTS
(error) ERR DB must be empty to perform CLUSTER FLUSHSLOTS.
> DEL foo
(integer) 1
> CLUSTER FLUSHSLOTS
OK
> CLUSTER INFO
"cluster_enabled:1\r\ncluster_state:fail\r\ncluster_slots_assigned:10923\r\n..."
> CLUSTER ADDSLOTSRANGE 10923 16383
OK
```
