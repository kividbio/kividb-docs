---
title: "CLIENT KILL"
description: "Closes connections."
version: "1.1"
command: "CLIENT KILL"
syntax: "CLIENT KILL ip:port | CLIENT KILL [ID id] [TYPE type] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]"
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
CLIENT KILL ip:port | CLIENT KILL [ID id] [TYPE type] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]
```

**Available since:** 1.1.0
<!-- generated: end -->
Closes connections. `CLIENT KILL ip:port` closes the one from that address. `CLIENT KILL` with filters closes every one that matches them: `ID`, `TYPE`, `USER`, `ADDR`, `LADDR`, `SKIPME` and `MAXAGE`, as for [`CLIENT LIST`](client-list.md). `SKIPME` is `yes` by default; with `no`, the connection sending it is closed too, after its reply. Closed connections get no reply.

## Reply

- The old form: `OK`, or `ERR No such client`.
- With filters: the number of connections closed.

## Examples

```
> CLIENT KILL ID 7
(integer) 1
> CLIENT KILL 1.2.3.4:5
(error) ERR No such client
```
