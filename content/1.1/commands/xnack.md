---
title: "XNACK"
description: "Release pending entries back to the group PEL without acknowledging, for immediate re-delivery."
version: "1.1"
command: "XNACK"
syntax: "XNACK key group <SILENT | FAIL | FATAL> IDS numids id [id ...] [RETRYCOUNT count] [FORCE]"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XNACK key group <SILENT | FAIL | FATAL> IDS numids id [id ...] [RETRYCOUNT count] [FORCE]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Release pending entries back to the group PEL without acknowledging, for immediate re-delivery. SILENT decrements the delivery counter, FAIL leaves it, FATAL pins it to LLONG_MAX; RETRYCOUNT overrides. FORCE creates unowned entries for non-pending IDs that exist in the stream
