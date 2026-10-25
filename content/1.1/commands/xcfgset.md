---
title: "XCFGSET"
description: "Set per-stream configuration; supported fields: MAX-ENTRIES n (persistent trim policy applied on every XADD, 0 clears the policy), MAX-DELETED-ENTRY-ID id (advance the tracked max deleted ID, never m…"
version: "1.1"
command: "XCFGSET"
syntax: "XCFGSET key field value [field value ...]"
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
XCFGSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Set per-stream configuration; supported fields: `MAX-ENTRIES n` (persistent trim policy applied on every XADD, `0` clears the policy), `MAX-DELETED-ENTRY-ID id` (advance the tracked max deleted ID, never moves backwards), `IDMP-DURATION seconds` and `IDMP-MAXSIZE n` (how long, and how many, idempotent ids are remembered per producer; defaults from `stream-idmp-duration` / `stream-idmp-maxsize`)
