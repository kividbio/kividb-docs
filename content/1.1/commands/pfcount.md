---
title: "PFCOUNT"
description: "Return the approximated cardinality of the set observed by the HyperLogLog at key; with multiple keys, returns the cardinality of the union by merging into a temporary HyperLogLog without persisting…"
version: "1.1"
command: "PFCOUNT"
syntax: "PFCOUNT key [key ...]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["hyperloglog", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PFCOUNT key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hyperloglog`, `@read`, `@slow`
<!-- generated: end -->
## Description

Return the approximated cardinality of the set observed by the HyperLogLog at `key`; with multiple keys, returns the cardinality of the union by merging into a temporary HyperLogLog without persisting it
