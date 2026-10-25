---
title: "XAUTOCLAIM"
description: "Scan and claim idle pending entries starting from start"
version: "1.2"
command: "XAUTOCLAIM"
syntax: "XAUTOCLAIM key group consumer min-idle-time start [COUNT count] [JUSTID]"
group: "stream"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XAUTOCLAIM key group consumer min-idle-time start [COUNT count] [JUSTID]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Scan and claim idle pending entries starting from `start`
