---
title: "XREADGROUP"
description: "Read new (>) or pending (specific ID) entries for a consumer; NOACK skips PEL tracking."
version: "1.1"
command: "XREADGROUP"
syntax: "XREADGROUP GROUP group consumer [COUNT n] [MAXCOUNT n] [MAXSIZE n] [BLOCK ms] [CLAIM min-idle-time] [NOACK] STREAMS key [key ...] id [id ...]"
group: "stream"
since: "1.1.0"
arity: -7
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "slow", "stream", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XREADGROUP GROUP group consumer [COUNT n] [MAXCOUNT n] [MAXSIZE n] [BLOCK ms] [CLAIM min-idle-time] [NOACK] STREAMS key [key ...] id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@slow`, `@stream`, `@write`
<!-- generated: end -->
## Description

Read new (`>`) or pending (specific ID) entries for a consumer; NOACK skips PEL tracking. `CLAIM` (Redis 8.4) also takes over entries pending for other consumers that have been idle that long, ahead of new ones; every entry then carries its idle time and delivery count. A group that does not exist is a `NOGROUP` error
