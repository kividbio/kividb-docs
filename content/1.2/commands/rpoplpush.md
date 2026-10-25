---
title: "RPOPLPUSH"
description: "Pop from tail of source, push to head of destination; deprecated alias for LMOVE"
version: "1.2"
command: "RPOPLPUSH"
syntax: "RPOPLPUSH source destination"
group: "list"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RPOPLPUSH source destination
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Pop from tail of source, push to head of destination; deprecated alias for LMOVE
