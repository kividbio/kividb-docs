---
title: "HEXPIRETIME"
description: "Per-field absolute Unix expiry in seconds; per-field returns: -2=no such field, -1=field has no TTL, otherwise Unix seconds"
version: "1.1"
command: "HEXPIRETIME"
syntax: "HEXPIRETIME key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HEXPIRETIME key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
## Description

Per-field absolute Unix expiry in seconds; per-field returns: `-2`=no such field, `-1`=field has no TTL, otherwise Unix seconds
