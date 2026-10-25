---
title: "PFMERGE"
description: "Merge one or more source HyperLogLogs into destkey by taking the element-wise maximum of all registers; missing source keys are treated as empty; AOF-logged"
version: "1.2"
command: "PFMERGE"
syntax: "PFMERGE destkey [sourcekey [sourcekey ...]]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["hyperloglog", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PFMERGE destkey [sourcekey [sourcekey ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@hyperloglog`, `@slow`, `@write`
<!-- generated: end -->
## Description

Merge one or more source HyperLogLogs into `destkey` by taking the element-wise maximum of all registers; missing source keys are treated as empty; AOF-logged
