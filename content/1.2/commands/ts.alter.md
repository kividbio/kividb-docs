---
title: "TS.ALTER"
description: "Changes a time series' retention, chunk size, duplicate policy or labels."
version: "1.2"
command: "TS.ALTER"
syntax: "TS.ALTER key [RETENTION ms] [CHUNK SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]"
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
TS.ALTER key [RETENTION ms] [CHUNK SIZE size] [DUPLICATE_POLICY policy] [LABELS label value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@timeseries`, `@write`
<!-- generated: end -->
Changes a time series' retention, chunk size, duplicate policy or labels. Labels given replace all of them, and the label index follows at once.

## Reply

- `OK`.

## Examples

```
> TS.ALTER temp:1 RETENTION 60000 LABELS room kitchen kind temp floor 1
OK
```
