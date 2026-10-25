---
title: "ZINCRBY"
description: "Increment a member's score; returns new score"
version: "1.1"
command: "ZINCRBY"
syntax: "ZINCRBY key increment member"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZINCRBY key increment member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
## Description

Increment a member's score; returns new score
