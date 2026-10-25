---
title: "CLIENT LIST"
description: "Return one line per connection, in Redis's layout (id, addr, laddr, name, age, idle, flags, db, sub, psub, ssub, multi, watch, cmd, user, redir, resp, lib-name, lib-ver, …), filtered as asked"
version: "1.2"
command: "CLIENT LIST"
syntax: "CLIENT LIST [TYPE normal|master|replica|pubsub] [ID id [id ...]] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]"
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
CLIENT LIST [TYPE normal|master|replica|pubsub] [ID id [id ...]] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return one line per connection, in Redis's layout (`id`, `addr`, `laddr`, `name`, `age`, `idle`, `flags`, `db`, `sub`, `psub`, `ssub`, `multi`, `watch`, `cmd`, `user`, `redir`, `resp`, `lib-name`, `lib-ver`, …), filtered as asked
