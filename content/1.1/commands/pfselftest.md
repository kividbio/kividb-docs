---
title: "PFSELFTEST"
description: "Run internal correctness tests of the HyperLogLog implementation: verifies empty cardinality returns 0, estimation accuracy is within 2% for 10,000 elements, and register encode/decode round-trips co…"
version: "1.1"
command: "PFSELFTEST"
syntax: "PFSELFTEST"
group: "hyperloglog"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "hyperloglog", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PFSELFTEST
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@hyperloglog`, `@read`, `@slow`
<!-- generated: end -->
## Description

Run internal correctness tests of the HyperLogLog implementation: verifies empty cardinality returns 0, estimation accuracy is within 2% for 10,000 elements, and register encode/decode round-trips correctly; returns OK on success or an error describing the failure
