---
title: "XADD"
description: "Append an entry; * auto-generates ID as ms-seq; NOMKSTREAM skips creation if key absent; MAXLEN/MINID trim the stream after insert, and KEEPREF / DELREF / ACKED say what trimming does with entries co…"
version: "1.1"
command: "XADD"
syntax: "XADD key [NOMKSTREAM] [KEEPREF | DELREF | ACKED] [IDMPAUTO producer-id | IDMP producer-id idempotent-id] [MAXLEN|MINID [=|~] threshold [LIMIT count]] *|id field value [...]"
group: "stream"
since: "1.1.0"
arity: -5
flags: ["fast", "write"]
acl_categories: ["fast", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XADD key [NOMKSTREAM] [KEEPREF | DELREF | ACKED] [IDMPAUTO producer-id | IDMP producer-id idempotent-id] [MAXLEN|MINID [=|~] threshold [LIMIT count]] *|id field value [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@stream`, `@write`
<!-- generated: end -->
## Description

Append an entry; `*` auto-generates ID as `ms-seq`; NOMKSTREAM skips creation if key absent; MAXLEN/MINID trim the stream after insert, and `KEEPREF` / `DELREF` / `ACKED` say what trimming does with entries consumer groups still reference. `IDMP` / `IDMPAUTO` (Redis 8.6) make the add idempotent: a retry by the same producer with the same id — or, with `IDMPAUTO`, the same content — adds nothing and returns the original entry's ID
