---
title: "BRPOPLPUSH"
description: "Blocking RPOPLPUSH; deprecated, use BLMOVE instead"
version: "1.2"
command: "BRPOPLPUSH"
syntax: "BRPOPLPUSH source destination timeout"
group: "list"
since: "1.1.0"
arity: 4
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
BRPOPLPUSH source destination timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Blocking RPOPLPUSH; deprecated, use BLMOVE instead
