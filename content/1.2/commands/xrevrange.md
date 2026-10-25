---
title: "XREVRANGE"
description: "Same as XRANGE but in reverse order"
version: "1.2"
command: "XREVRANGE"
syntax: "XREVRANGE key end start [COUNT count]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XREVRANGE key end start [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
## Description

Same as XRANGE but in reverse order
