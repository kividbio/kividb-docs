---
title: "SETRANGE"
description: "Overwrite bytes at offset; zero-pads if key is shorter than offset"
version: "1.1"
command: "SETRANGE"
syntax: "SETRANGE key offset value"
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
SETRANGE key offset value
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
## Description

Overwrite bytes at offset; zero-pads if key is shorter than offset
