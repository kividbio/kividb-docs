---
title: "XREAD"
description: "Read new entries across multiple streams; $ means entries added after this call and + the last entry; BLOCK suspends until new data arrives or timeout."
version: "1.2"
command: "XREAD"
syntax: "XREAD [COUNT count] [MAXCOUNT maxcount] [MAXSIZE maxsize] [BLOCK ms] STREAMS key [key ...] id [id ...]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["blocking", "movablekeys", "readonly"]
acl_categories: ["blocking", "read", "slow", "stream"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XREAD [COUNT count] [MAXCOUNT maxcount] [MAXSIZE maxsize] [BLOCK ms] STREAMS key [key ...] id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@read`, `@slow`, `@stream`
<!-- generated: end -->
## Description

Read new entries across multiple streams; `$` means entries added after this call and `+` the last entry; BLOCK suspends until new data arrives or timeout. `COUNT` is per stream; `MAXCOUNT` and `MAXSIZE` (Redis 8.10) cap the entries and the bytes of the whole reply
