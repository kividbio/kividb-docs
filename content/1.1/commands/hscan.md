---
title: "HSCAN"
description: "Incrementally iterate fields and values; NOVALUES returns field names only."
version: "1.1"
command: "HSCAN"
syntax: "HSCAN key cursor [MATCH pattern] [COUNT count] [NOVALUES]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HSCAN key cursor [MATCH pattern] [COUNT count] [NOVALUES]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
## Description

Incrementally iterate fields and values; `NOVALUES` returns field names only. Cursors are stable positions, as for `SCAN`
