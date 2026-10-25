---
title: "XACK"
description: "Acknowledge processed entries; removes from PEL"
version: "1.2"
command: "XACK"
syntax: "XACK key group id [id ...]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XACK key group id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@stream`, `@write`
<!-- generated: end -->
## Description

Acknowledge processed entries; removes from PEL
