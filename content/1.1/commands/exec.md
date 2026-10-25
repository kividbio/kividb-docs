---
title: "EXEC"
description: "Execute all queued commands atomically; returns nil if a WATCHed key was modified"
version: "1.1"
command: "EXEC"
syntax: "EXEC"
group: "transaction"
since: "1.1.0"
arity: 1
flags: []
acl_categories: ["slow", "transaction"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
EXEC
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@transaction`
<!-- generated: end -->
## Description

Execute all queued commands atomically; returns nil if a `WATCH`ed key was modified
