---
title: "PFADD"
description: "Add one or more elements to the HyperLogLog; creates the key if it does not exist; returns 1 if the internal representation was modified (cardinality estimate changed), 0 otherwise; calling with no e…"
version: "1.1"
command: "PFADD"
syntax: "PFADD key [element [element ...]]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "hyperloglog", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PFADD key [element [element ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hyperloglog`, `@write`
<!-- generated: end -->
## Description

Add one or more elements to the HyperLogLog; creates the key if it does not exist; returns 1 if the internal representation was modified (cardinality estimate changed), 0 otherwise; calling with no elements creates the key (returns 1) or is a no-op if it exists (returns 0); AOF-logged
