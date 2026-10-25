---
title: "HINCRBY"
description: "Increment an integer field; initialises to 0 if absent"
version: "1.2"
command: "HINCRBY"
syntax: "HINCRBY key field increment"
group: "hash"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HINCRBY key field increment
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
## Description

Increment an integer field; initialises to 0 if absent
