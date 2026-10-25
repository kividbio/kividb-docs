---
title: "XACKDEL"
description: "Acknowledge and delete entries in one step (Redis 8.2)."
version: "1.1"
command: "XACKDEL"
syntax: "XACKDEL key group [KEEPREF | DELREF | ACKED] IDS numids id [id ...]"
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
XACKDEL key group [KEEPREF | DELREF | ACKED] IDS numids id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Acknowledge and delete entries in one step (Redis 8.2). Per id: `-1` not pending in this group, `1` acknowledged and deleted (or already gone), `2` acknowledged but kept because another group still references it (`ACKED` only). Policies as for `XDELEX`. The bare form `XACKDEL key group id [id ...]` is still accepted
