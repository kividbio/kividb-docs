---
title: "CLUSTER FLUSHSLOTS"
description: "Clears this node's slot table: afterwards it owns no slots."
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
Clears this node's slot table: afterwards it owns no slots. Use it on a node being rebuilt by hand, before [`CLUSTER ADDSLOTSRANGE`](cluster-addslotsrange.md) gives it a new set.

It differs from Redis in two ways:

- It clears every slot in this node's view, not only its own. The other masters' slots come back within a few seconds, from their heartbeats; until then the node's `cluster_state` is `fail` and it answers keyed commands with `CLUSTERDOWN`. Redis removes only the node's own slots.
- It does not require an empty database. Redis refuses with `DB must be empty to perform CLUSTER FLUSHSLOTS` when the node holds keys. KiviDB keeps the keys, and does not serve them until the slots they hash to are assigned back to the node.

Only this node's view changes: the other nodes still send clients to it for its old slots, and it answers them with `CLUSTERDOWN Hash slot n is not served`. To move a master's slots to another master with their keys, reshard instead, as in [Adding a master and moving slots](../guides/cluster.md#adding-a-master-and-moving-slots).

## Reply

`OK`, or `ERR This instance has cluster support disabled` on a server that is not a cluster node.

## Examples

```
> SET foo bar
OK
> CLUSTER FLUSHSLOTS
OK
> CLUSTER INFO
"cluster_enabled:1\r\ncluster_state:fail\r\ncluster_slots_assigned:0\r\n..."
> DBSIZE
(integer) 1
> GET foo
(error) CLUSTERDOWN Hash slot 12182 is not served
> CLUSTER ADDSLOTSRANGE 10923 16383
OK
> GET foo
"bar"
```
