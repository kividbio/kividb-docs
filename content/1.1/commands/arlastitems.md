---
title: "ARLASTITEMS"
description: "The most recently inserted elements, oldest-first by default, newest-first with REV."
version: "1.1"
command: "ARLASTITEMS"
syntax: "ARLASTITEMS key count [REV]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARLASTITEMS key count [REV]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

The most recently inserted elements, oldest-first by default, newest-first with `REV`. Wraps within the window for ring buffers
