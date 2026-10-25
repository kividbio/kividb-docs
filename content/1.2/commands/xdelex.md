---
title: "XDELEX"
description: "Delete entries with control over consumer-group references (Redis 8.2)."
version: "1.2"
command: "XDELEX"
syntax: "XDELEX key [KEEPREF | DELREF | ACKED] IDS numids id [id ...]"
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
XDELEX key [KEEPREF | DELREF | ACKED] IDS numids id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Delete entries with control over consumer-group references (Redis 8.2). Per id: `-1` no such entry, `1` deleted, `2` kept because a group still references it (`ACKED` only). `KEEPREF` (default) deletes and leaves pending-list references; `DELREF` deletes and removes them from every group; `ACKED` deletes only an entry every group has read and acknowledged. The policy may also follow the `IDS` block; `REF` is accepted as an older name for `ACKED`
