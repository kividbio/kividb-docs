---
title: "TS.DECRBY"
description: "TS.INCRBY, subtracting."
version: "1.2"
command: "TS.DECRBY"
syntax: "TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]"
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
TS.DECRBY key value [TIMESTAMP timestamp] [RETENTION ms] [CHUNK SIZE size] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
[`TS.INCRBY`](ts.incrby.md), subtracting.

## Examples

```
> TS.DECRBY ctr 1 TIMESTAMP 3000
(integer) 3000
```
