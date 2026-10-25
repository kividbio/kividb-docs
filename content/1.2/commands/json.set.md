---
title: "JSON.SET"
description: "Set every value the path matches; if it matches nothing and ends in a member name under a single existing object, add that member."
version: "1.2"
command: "JSON.SET"
syntax: "JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Set every value the path matches; if it matches nothing and ends in a member name under a single existing object, add that member. `NX` = only if the path matches nothing, `XX` = only if it matches. A new key must be created at the root. `FPHA` (Redis 8.8) sets the floating-point type arrays of floats are held in. Returns `OK`, or nil if nothing was set
