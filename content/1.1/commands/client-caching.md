---
title: "CLIENT CACHING"
description: "yes is accepted only in OPTIN mode and no only in OPTOUT mode, with Redis's errors otherwise."
version: "1.1"
command: "CLIENT CACHING"
syntax: "CLIENT CACHING yes|no"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLIENT CACHING yes|no
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

`yes` is accepted only in `OPTIN` mode and `no` only in `OPTOUT` mode, with Redis's errors otherwise. Set a single-shot opt-in or opt-out flag for the next data read command. In OPTIN mode: `yes` registers the next read for invalidation tracking. In OPTOUT mode: `no` suppresses registration for the next read. The flag is consumed by exactly one data command then cleared. Has no effect outside OPTIN/OPTOUT mode
