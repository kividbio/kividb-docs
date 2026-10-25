---
title: "HELLO"
description: "Switch the connection to RESP2 or RESP3 and return the server's details (server, version, proto, id, mode, role, modules) — a map under RESP3."
version: "1.2"
command: "HELLO"
syntax: "HELLO [protover [AUTH username password] [SETNAME clientname]]"
group: "server"
since: "1.1.0"
arity: -1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HELLO [protover [AUTH username password] [SETNAME clientname]]
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
## Description

Switch the connection to RESP2 or RESP3 and return the server's details (`server`, `version`, `proto`, `id`, `mode`, `role`, `modules`) — a map under RESP3. `AUTH` and `SETNAME` apply before the reply. Unauthenticated, when a password is required, it is `NOAUTH`
