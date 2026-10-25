---
title: "HPERSIST"
description: "Remove per-field TTLs; per-field returns: -2=no such field, -1=field has no TTL, 1=TTL removed"
version: "1.2"
command: "HPERSIST"
syntax: "HPERSIST key FIELDS numfields field [field ...]"
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
HPERSIST key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
## Description

Remove per-field TTLs; per-field returns: `-2`=no such field, `-1`=field has no TTL, `1`=TTL removed
