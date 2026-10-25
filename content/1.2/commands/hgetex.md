---
title: "HGETEX"
description: "Atomically read fields and optionally manipulate per-field TTLs; returns array of values, nil for missing fields"
version: "1.2"
command: "HGETEX"
syntax: "HGETEX key [EX seconds | PX ms | EXAT unix-secs | PXAT unix-ms | PERSIST] FIELDS numfields field [field ...]"
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
HGETEX key [EX seconds | PX ms | EXAT unix-secs | PXAT unix-ms | PERSIST] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Atomically read fields and optionally manipulate per-field TTLs; returns array of values, nil for missing fields
