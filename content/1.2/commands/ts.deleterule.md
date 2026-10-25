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
Deletes the compaction rule from `sourceKey` to `destKey`. Both series stay.

## Reply

- `OK`.
