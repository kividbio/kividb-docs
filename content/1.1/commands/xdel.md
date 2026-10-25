---
title: "XDEL"
description: "Delete entries by ID; returns count deleted"
version: "1.1"
command: "XDEL"
syntax: "XDEL key id [id ...]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XDEL key id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Delete entries by ID; returns count deleted
