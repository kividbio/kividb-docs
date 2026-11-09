---
title: "CLIENT"
description: "Inspects and manages client connections."
version: "1.2"
command: "CLIENT"
syntax: "CLIENT"
group: "server"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["connection", "slow"]
history: []
subcommands: ["CLIENT CACHING", "CLIENT GETNAME", "CLIENT GETREDIR", "CLIENT HELP", "CLIENT ID", "CLIENT INFO", "CLIENT KILL", "CLIENT LIST", "CLIENT NO-EVICT", "CLIENT NO-TOUCH", "CLIENT PAUSE", "CLIENT REPLY", "CLIENT SETINFO", "CLIENT SETNAME", "CLIENT TRACKING", "CLIENT TRACKINGINFO", "CLIENT UNBLOCK", "CLIENT UNPAUSE"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@slow`

Subcommands: [CLIENT CACHING](client-caching.md), [CLIENT GETNAME](client-getname.md), [CLIENT GETREDIR](client-getredir.md), [CLIENT HELP](client-help.md), [CLIENT ID](client-id.md), [CLIENT INFO](client-info.md), [CLIENT KILL](client-kill.md), [CLIENT LIST](client-list.md), [CLIENT NO-EVICT](client-no-evict.md), [CLIENT NO-TOUCH](client-no-touch.md), [CLIENT PAUSE](client-pause.md), [CLIENT REPLY](client-reply.md), [CLIENT SETINFO](client-setinfo.md), [CLIENT SETNAME](client-setname.md), [CLIENT TRACKING](client-tracking.md), [CLIENT TRACKINGINFO](client-trackinginfo.md), [CLIENT UNBLOCK](client-unblock.md), [CLIENT UNPAUSE](client-unpause.md)
<!-- generated: end -->
`CLIENT` is a container: the work is done by its subcommands, which look at and manage the connections to the server, the one sending them included.

| Subcommand | |
|---|---|
| [`CLIENT ID`](client-id.md), [`CLIENT INFO`](client-info.md), [`CLIENT LIST`](client-list.md) | who is connected, and what each connection is doing |
| [`CLIENT SETNAME`](client-setname.md), [`CLIENT GETNAME`](client-getname.md), [`CLIENT SETINFO`](client-setinfo.md) | label a connection, so that it can be found in `CLIENT LIST` |
| [`CLIENT KILL`](client-kill.md), [`CLIENT UNBLOCK`](client-unblock.md) | close a connection, or end its blocking command |
| [`CLIENT PAUSE`](client-pause.md), [`CLIENT UNPAUSE`](client-unpause.md) | hold every client's commands, or just writes, for a while |
| [`CLIENT REPLY`](client-reply.md) | turn off the replies to this connection |
| [`CLIENT TRACKING`](client-tracking.md), [`CLIENT CACHING`](client-caching.md), [`CLIENT TRACKINGINFO`](client-trackinginfo.md), [`CLIENT GETREDIR`](client-getredir.md) | [client-side caching](../guides/client-side-caching.md) |
| [`CLIENT NO-EVICT`](client-no-evict.md), [`CLIENT NO-TOUCH`](client-no-touch.md) | accepted for compatibility |
| [`CLIENT HELP`](client-help.md) | the list, from the server |

`CLIENT` alone, or with a name that is not one of these, is an error.

## Examples

```
> CLIENT
(error) ERR wrong number of arguments for 'client' command
> CLIENT NOPE
(error) ERR unknown subcommand 'NOPE'. Try CLIENT HELP.
```
