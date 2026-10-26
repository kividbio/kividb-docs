---
title: "TS.REVRANGE"
description: "TS.RANGE, newest first, with the same options."
version: "1.1"
command: "TS.REVRANGE"
syntax: "TS.REVRANGE key fromTimestamp toTimestamp [...]"
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
TS.REVRANGE key fromTimestamp toTimestamp [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@timeseries`
<!-- generated: end -->
[`TS.RANGE`](ts.range.md), newest first, with the same options.

## Examples

```
> TS.REVRANGE temp:1 - + COUNT 2
1) 1) (integer) 4000
   2) "23"
2) 1) (integer) 3000
   2) "22.5"
```
