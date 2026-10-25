---
title: "HEXPIRE"
description: "Set per-field TTLs in seconds; per-field returns: -2=no such field, 0=condition not met, 1=TTL set, 2=field deleted (past time)"
version: "1.1"
command: "HEXPIRE"
syntax: "HEXPIRE key seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HEXPIRE key seconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set per-field TTLs in seconds; per-field returns: `-2`=no such field, `0`=condition not met, `1`=TTL set, `2`=field deleted (past time)
