---
title: "CLUSTER SLOT-STATS"
description: "Returns statistics for each slot this node owns: for slots start to end, or for the n first by metric (LIMIT defaults to 16384)."
version: "1.1"
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

## Known issue

`ORDERBY` with neither `ASC` nor `DESC` sorts ascending, where Redis sorts descending, so it returns the emptiest slots. Give `DESC` for the busiest. Filed as [kividb#139](https://github.com/kividbio/kividb/issues/139), fixed in 1.2.

## Reply

- Per slot, its number and its statistics.
- `ERR ORDERBY metric 'name' not supported (use 'key-count')`.

## Examples

```
> CLUSTER SLOT-STATS SLOTSRANGE 15495 15496
1) 1) (integer) 15495
   2) 1) "key-count"
      2) (integer) 2
      3) "cpu-usec"
      4) (integer) 0
      5) "network-bytes-in"
      6) (integer) 0
      7) "network-bytes-out"
      8) (integer) 0
2) 1) (integer) 15496
   2) 1) "key-count"
      2) (integer) 0
      ...
> CLUSTER SLOT-STATS ORDERBY key-count LIMIT 1 DESC
1) 1) (integer) 325
   2) 1) "key-count"
      2) (integer) 1
      ...
```
