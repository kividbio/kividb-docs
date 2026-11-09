---
title: "CLIENT UNBLOCK"
description: "Accepted for compatibility, and replies 0: KiviDB does not unblock a client waiting in a blocking command this way."
version: "1.2"
command: "CLIENT UNBLOCK"
syntax: "CLIENT UNBLOCK id"
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
CLIENT UNBLOCK id
```

**Available since:** 1.1.0
<!-- generated: end -->
Ends the blocking command another connection is waiting in, such as [`BLPOP`](blpop.md), `BLMOVE`, `BZPOPMIN` or `XREAD BLOCK`, as if its timeout had passed. `id` is that connection's [`CLIENT ID`](client-id.md).

- `TIMEOUT`, the default: the blocked command returns what it returns on a timeout, usually `nil`.
- `ERROR`: it fails with `-UNBLOCKED client unblocked via CLIENT UNBLOCK`.

Use it to stop a worker waiting on an empty queue, for example to shut it down, without closing its connection.

## Reply

`1` if the connection was blocked and has been released; `0` if there is no such connection or it was not blocked.

## Examples

```
client 2> BLPOP jobs 0
client 1> CLIENT UNBLOCK 2
(integer) 1
client 2> (nil)
client 1> CLIENT UNBLOCK 2
(integer) 0
client 1> CLIENT UNBLOCK abc
(error) ERR value is not an integer or out of range
```
