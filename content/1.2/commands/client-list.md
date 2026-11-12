---
title: "CLIENT LIST"
description: "Returns a line per connection, with Redis's fields: id, addr, laddr, name, age, idle, flags, db, sub, psub, ssub, multi, watch, cmd, user, redir, resp, lib-name, lib-ver and others."
version: "1.2"
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

`flags` is `N` for an ordinary client, `S` on a master for a replica's replication link, `M` on a replica for its link to its master, `b` for a client blocked in a command such as `BLPOP` or `WAIT`, `P` for a Pub/Sub subscriber, and `e` with [`CLIENT NO-EVICT`](client-no-evict.md) on. `laddr` is the address the client connected to. The replication links show as `S` and `M` since 1.2.1, so that `TYPE replica` and `TYPE master` find them; in 1.2.0 they showed as `N`. `e`, and `b` for every blocked client, are since 1.2.1 too.
