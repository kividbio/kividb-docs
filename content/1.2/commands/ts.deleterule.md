---
title: "TS.DELETERULE"
description: "Deletes the compaction rule from sourceKey to destKey."
version: "1.2"
command: "TS.DELETERULE"
syntax: "TS.DELETERULE sourceKey destKey"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "timeseries", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.DELETERULE sourceKey destKey
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Deletes the compaction rule from `sourceKey` to `destKey` that [`TS.CREATERULE`](ts.createrule.md) made. Samples added to the source after it are no longer aggregated into the destination.

Both series stay. The destination keeps the samples written to it so far, but not the bucket that was still open: that bucket is never written. The destination is no longer a compaction of the source, so [`TS.INFO`](ts.info.md) shows its `sourceKey` as `nil`, and it can be the destination of another rule.

## Reply

- `OK`.
- `TSDB: compaction rule does not exist` if there is no rule between the two.
- `TSDB: the key does not exist` if `sourceKey` is missing.

## Examples

```
> TS.CREATE src
OK
> TS.CREATE src:avg
OK
> TS.CREATERULE src src:avg AGGREGATION avg 1000
OK
> TS.ADD src 100 1
(integer) 100
> TS.ADD src 1100 3
(integer) 1100
> TS.DELETERULE src src:avg
OK
> TS.DELETERULE src src:avg
(error) TSDB: compaction rule does not exist
> TS.RANGE src:avg - +
1) 1) (integer) 0
   2) 1
```
