---
title: "CLUSTER SLOT-STATS"
description: "Returns statistics for each slot this node owns: for slots start to end, or for the n first by metric (LIMIT defaults to 16384)."
version: "1.2"
command: "CLUSTER SLOT-STATS"
syntax: "CLUSTER SLOT-STATS SLOTSRANGE start end\nCLUSTER SLOT-STATS ORDERBY metric [LIMIT n] [ASC | DESC]"
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
CLUSTER SLOT-STATS SLOTSRANGE start end
CLUSTER SLOT-STATS ORDERBY metric [LIMIT n] [ASC | DESC]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns statistics for each slot this node owns: for slots `start` to `end`, or for the `n` first by `metric` (`LIMIT` defaults to 16384).

Each slot has `key-count`, `cpu-usec`, `network-bytes-in` and `network-bytes-out`. Only `key-count` is measured; the other three are `0`, and `ORDERBY` takes only `key-count`.

`ORDERBY` sorts descending, the busiest slots first, unless given `ASC`. Before 1.2, it sorted ascending unless given `DESC`, so `ORDERBY key-count LIMIT n` returned empty slots.

## Reply

- Per slot, its number and its statistics.
- `ERR ORDERBY metric 'name' not supported (use 'key-count')`.

## Examples

```
> CLUSTER SLOT-STATS SLOTSRANGE 10778 10779
1) 1) (integer) 10778
   2) 1) "key-count"
      2) (integer) 2
      3) "cpu-usec"
      4) (integer) 0
      5) "network-bytes-in"
      6) (integer) 0
      7) "network-bytes-out"
      8) (integer) 0
2) 1) (integer) 10779
   2) 1) "key-count"
      2) (integer) 0
      ...
> CLUSTER SLOT-STATS ORDERBY key-count LIMIT 2
1) 1) (integer) 10778
   2) 1) "key-count"
      2) (integer) 2
      ...
2) 1) (integer) 12182
   2) 1) "key-count"
      2) (integer) 1
      ...
```
