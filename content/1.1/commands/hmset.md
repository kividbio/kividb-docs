---
title: "HMSET"
description: "Deprecated alias for HSET; always returns OK"
version: "1.1"
command: "HMSET"
syntax: "HMSET key field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HMSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
## Description

Deprecated alias for `HSET`; always returns OK
