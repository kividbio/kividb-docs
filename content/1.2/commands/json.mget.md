---
title: "JSON.MGET"
description: "The path evaluated against each key, as JSON text; nil for a missing key or one of another type"
version: "1.2"
command: "JSON.MGET"
syntax: "JSON.MGET key [key ...] path"
group: "json"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.MGET key [key ...] path
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
## Description

The path evaluated against each key, as JSON text; nil for a missing key or one of another type
