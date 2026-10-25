---
title: "SSCAN"
description: "Incrementally iterate members; cursor 0 begins and ends a full iteration."
version: "1.2"
command: "SSCAN"
syntax: "SSCAN key cursor [MATCH pattern] [COUNT count]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SSCAN key cursor [MATCH pattern] [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Incrementally iterate members; cursor 0 begins and ends a full iteration. Cursors are stable positions, as for `SCAN`
