---
title: "CLUSTER ADDSLOTSRANGE"
description: "Makes this node the owner of every slot from start to end, both included, for each pair given."
version: "1.2"
command: "CLUSTER ADDSLOTSRANGE"
syntax: "CLUSTER ADDSLOTSRANGE start end [start end ...]"
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
CLUSTER ADDSLOTSRANGE start end [start end ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node the owner of every slot from `start` to `end`, both included, for each pair given. It is [`CLUSTER ADDSLOTS`](cluster-addslots.md) for ranges: the way to give a new master its share of the 16384 slots by hand, after [`CLUSTER MEET`](cluster-meet.md), without listing thousands of slot numbers. See [Creating a cluster](../guides/cluster.md#creating-a-cluster).

- `start`, `end`: slot numbers from `0` to `16383`, with `start` not above `end`. A range of one slot is `n n`.
- Several pairs can be given in one call.

A slot that any node already owns is refused with `Slot n is already busy`, and ranges that overlap with `Slot n specified multiple times`. Every range is checked before any is claimed, as in Redis: when a call fails, it claimed nothing. That is since 1.2.1; in 1.2.0, the ranges were claimed in order, those before the one that failed stayed claimed, and an overlap was reported as busy.

The other nodes learn of the new owner from this node's heartbeats. On success the node saves [`nodes.conf`](../reference/configuration.md#cluster-config-file).

## Reply

`OK`.

## Errors

- `ERR Slot n is already busy`: the slot is owned, by this node or another.
- `ERR Slot n specified multiple times`: two ranges overlap.
- `ERR start slot number start is greater than end slot number end`: `start` is above `end` (`ERR Invalid range start-end` before 1.2.1).
- `ERR Invalid slot n, must be between 0 and 16383`.
- `ERR wrong number of arguments for 'cluster|addslotsrange' command`: no pair, or an odd number of slot numbers.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER ADDSLOTSRANGE 0 99 50 120
(error) ERR Slot 50 specified multiple times
> CLUSTER SLOTS
(empty array)
> CLUSTER ADDSLOTSRANGE 0 5460
OK
> CLUSTER ADDSLOTSRANGE 10 5
(error) ERR start slot number 10 is greater than end slot number 5
```
