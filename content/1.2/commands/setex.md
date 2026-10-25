---
title: "SETEX"
description: "Set a key with a TTL in seconds"
version: "1.2"
command: "SETEX"
syntax: "SETEX key seconds value"
group: "string"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SETEX key seconds value
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Set a key with a TTL in seconds
