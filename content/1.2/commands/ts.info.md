---
title: "TS.INFO"
description: "Returns a time series' metadata: its number of samples, memory use, first and last timestamps, retention, chunk size, duplicate policy, labels, the series it is compacted from (sourceKey, nil if none…"
version: "1.2"
command: "TS.INFO"
syntax: "TS.INFO key [DEBUG]"
group: "time-series"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "timeseries"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TS.INFO key [DEBUG]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
Returns a time series' metadata: its number of samples, memory use, first and last timestamps, retention, chunk size, duplicate policy, labels, the series it is compacted from (`sourceKey`, nil if none), and its compaction rules. `sourceKey` is new in 1.2.

## Examples

```
> TS.CREATE a
OK
> TS.INFO a
 1) "totalSamples"
 2) "0"
 3) "memoryUsage"
 4) "0"
 5) "firstTimestamp"
 6) "0"
 7) "lastTimestamp"
 8) "0"
 9) "retentionTime"
10) "0"
11) "chunkSize"
12) "4096"
13) "duplicatePolicy"
14) "last"
15) "labels"
16) (empty array)
17) "sourceKey"
18) (nil)
19) "rules"
20) (empty array)
```
