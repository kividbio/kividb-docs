---
title: "TS.INFO"
description: "Returns a time series' metadata: its number of samples, memory use, first and last timestamps, retention, chunk size, duplicate policy, labels, and compaction rules."
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
Returns a time series' metadata: its number of samples, memory use, first and last timestamps, retention, chunk size, duplicate policy, labels, and compaction rules.

## Examples

```
> TS.CREATE a
OK
> TS.INFO a
 1) totalSamples
 2) "0"
 ...
13) duplicatePolicy
14) last
 ...
```
