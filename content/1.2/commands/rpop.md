---
title: "RPOP"
description: "Remove and return the last element; with count returns an array of up to count elements"
version: "1.2"
command: "RPOP"
syntax: "RPOP key [count]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "list", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RPOP key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
## Description

Remove and return the last element; with count returns an array of up to count elements
