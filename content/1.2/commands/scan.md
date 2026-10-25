---
title: "SCAN"
description: "Cursor-based incremental key iteration; cursor 0 starts and ends a full cycle; MATCH filters by glob pattern (Redis's matching rules); COUNT is a hint for page size (default 10); TYPE returns only ke…"
version: "1.2"
command: "SCAN"
syntax: "SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]"
group: "generic"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SCAN cursor [MATCH pattern] [COUNT count] [TYPE type]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Cursor-based incremental key iteration; cursor `0` starts and ends a full cycle; `MATCH` filters by glob pattern (Redis's matching rules); `COUNT` is a hint for page size (default 10); `TYPE` returns only keys of that type; returns `[next-cursor, [keys...]]`. A cursor is a position in a stable order of key hashes, so a key present for the whole scan is returned whatever is added or removed meanwhile. Cursors from 1.0.4 or earlier are not valid
