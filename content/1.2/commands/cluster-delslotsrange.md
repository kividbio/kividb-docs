---
title: "CLUSTER DELSLOTSRANGE"
description: "Makes this node give up every slot from start to end, both included, for each pair given."
version: "1.2"
command: "CLUSTER DELSLOTSRANGE"
syntax: "CLUSTER DELSLOTSRANGE start end [start end ...]"
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
CLUSTER DELSLOTSRANGE start end [start end ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node give up every slot from `start` to `end`, both included, for each pair given. It is [`CLUSTER DELSLOTS`](cluster-delslots.md) for ranges, and behaves the same way: it removes a slot from this node's view of the cluster whoever owns it, and drops the slot's `IMPORTING` state.

All the ranges are checked before any slot is released. If a slot is not assigned, or appears in two ranges, the call is refused and nothing changes, as in Redis.

Only this node's view changes. The other nodes keep the old owner. While a slot has no owner in this node's view, the node's `cluster_state` is `fail` and it answers keyed commands with `CLUSTERDOWN`, unless [`cluster-require-full-coverage`](../reference/configuration.md#cluster-require-full-coverage) is `no`. [`CLUSTER ADDSLOTSRANGE`](cluster-addslotsrange.md) on the node gives the slots back to it.

## Reply

`OK`.

## Errors

- `ERR Slot n is already unassigned`.
- `ERR Slot n specified multiple times`: two ranges overlap.
- `ERR Invalid range start-end`: `start` is above `end`.
- `ERR Invalid slot n, must be between 0 and 16383`.
- `ERR wrong number of arguments for 'cluster|delslotsrange' command`: no pair, or an odd number of slot numbers.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER DELSLOTSRANGE 16000 16010 16005 16020
(error) ERR Slot 16005 specified multiple times
> CLUSTER DELSLOTSRANGE 16000 16010
OK
> CLUSTER DELSLOTSRANGE 16100 16110 16000 16010
(error) ERR Slot 16000 is already unassigned
> SET foo bar
(error) CLUSTERDOWN The cluster is down
```

The third call left slots 16100 to 16110 as they were.
