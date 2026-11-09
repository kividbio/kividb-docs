---
title: "CLIENT INFO"
description: "Returns this connection's line of CLIENT LIST: its ID, address, name, database, the last command it ran, its user, its protocol (resp=2 or resp=3), the library it reported with CLIENT SETINFO, and it…"
version: "1.2"
command: "CLIENT INFO"
syntax: "CLIENT INFO"
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
CLIENT INFO
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this connection's line of [`CLIENT LIST`](client-list.md): its ID, address, name, database, the last command it ran, its user, its protocol (`resp=2` or `resp=3`), the library it reported with [`CLIENT SETINFO`](client-setinfo.md), and its counters. The fields are described on the `CLIENT LIST` page.

It is the cheap way for a connection to see itself: no other connection is looked at.

`laddr` is the address the server listens on, such as `0.0.0.0:6380` when it listens on every interface, rather than the address this connection reached.

## Reply

One line, as a bulk string ending in a newline.

## Examples

```
> CLIENT SETNAME worker-1
OK
> CLIENT INFO
"id=1 addr=127.0.0.1:45906 laddr=0.0.0.0:6380 fd=0 name=worker-1 age=0 idle=0 flags=N db=0 ... cmd=client|info user=default redir=-1 resp=2 lib-name= lib-ver= ..."
```
