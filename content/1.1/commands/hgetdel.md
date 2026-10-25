---
title: "HGETDEL"
description: "Atomically read and delete fields; returns array of values, nil for missing fields"
version: "1.1"
command: "HGETDEL"
syntax: "HGETDEL key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HGETDEL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Atomically read and delete fields; returns array of values, nil for missing fields
