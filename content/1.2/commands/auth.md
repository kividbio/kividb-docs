---
title: "AUTH"
description: "Authenticate the connection; AUTH password (legacy) or AUTH username password (Redis 6 ACL form); required when --requirepass is set or when the user has a password; PING, AUTH, QUIT, HELLO, and RESE…"
version: "1.2"
command: "AUTH"
syntax: "AUTH [username] password"
group: "acl"
since: "1.1.0"
arity: -2
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
AUTH [username] password
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
## Description

Authenticate the connection; `AUTH password` (legacy) or `AUTH username password` (Redis 6 ACL form); required when `--requirepass` is set or when the user has a password; `PING`, `AUTH`, `QUIT`, `HELLO`, and `RESET` are always allowed before authentication. On success returns **`OK` as a bulk string** (`$2\r\nOK\r\n`), matching Redis—not a simple-string `+OK`
