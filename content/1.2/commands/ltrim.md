---
title: "LTRIM"
description: "Trim a list in-place to the specified inclusive range"
version: "1.2"
command: "LTRIM"
syntax: "LTRIM key start stop"
group: "list"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LTRIM key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Trim a list in-place to the specified inclusive range
