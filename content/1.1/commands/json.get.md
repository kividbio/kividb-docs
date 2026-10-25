---
title: "JSON.GET"
description: "No path: the whole document."
version: "1.1"
command: "JSON.GET"
syntax: "JSON.GET key [INDENT indent] [NEWLINE newline] [SPACE space] [path ...]"
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
JSON.GET key [INDENT indent] [NEWLINE newline] [SPACE space] [path ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
## Description

No path: the whole document. One path: a JSON array of its matches. Several: an object with one member per path. The three options format the output
