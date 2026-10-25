---
title: "SDIFF"
description: "Return members in the first set not present in any subsequent set."
version: "1.1"
command: "SDIFF"
syntax: "SDIFF key [key ...]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SDIFF key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Return members in the first set not present in any subsequent set. As for `SINTER` and `SUNION`, a key that does not exist is an empty set and a key of another type is a `WRONGTYPE` error
