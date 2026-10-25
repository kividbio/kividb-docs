---
title: "SADD"
description: "Add one or more members; returns count of new members added"
version: "1.2"
command: "SADD"
syntax: "SADD key member [member ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SADD key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
## Description

Add one or more members; returns count of new members added
