---
title: "CLIENT LIST"
description: "Returns a line per connection, with Redis's fields: id, addr, laddr, name, age, idle, flags, db, sub, psub, ssub, multi, watch, cmd, user, redir, resp, lib-name, lib-ver and others."
version: "1.1"
command: "CLIENT LIST"
syntax: "CLIENT LIST [TYPE normal|master|replica|pubsub] [ID id [id ...]] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT LIST [TYPE normal|master|replica|pubsub] [ID id [id ...]] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns a line per connection, with Redis's fields: `id`, `addr`, `laddr`, `name`, `age`, `idle`, `flags`, `db`, `sub`, `psub`, `ssub`, `multi`, `watch`, `cmd`, `user`, `redir`, `resp`, `lib-name`, `lib-ver` and others. The options keep only the connections that match.

| Option | Keeps |
|---|---|
| `TYPE normal \| master \| replica \| pubsub` | connections of this kind |
| `ID id ...` | these IDs |
| `USER username` | connections logged in as this user |
| `ADDR ip:port`, `LADDR ip:port` | the client's address, or the server's |
| `SKIPME yes \| no` | whether to leave this connection out |
| `MAXAGE seconds` | connections at most this old |
