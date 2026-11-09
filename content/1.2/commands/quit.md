---
title: "QUIT"
description: "Asks the server to close the connection."
version: "1.2"
command: "QUIT"
syntax: "QUIT"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["connection", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
QUIT
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@slow`
<!-- generated: end -->
Asks the server to close the connection. The server replies `OK`, then closes it. Commands sent after `QUIT` on the same connection, in a pipeline, are not run. Most clients close the socket themselves when they are done, without `QUIT`; it is there for clients that want the server to confirm, and for scripts piping commands through a terminal.

`QUIT` is accepted in any state: before [`AUTH`](auth.md) on a server that requires a password, while the connection is subscribed to channels, and inside a transaction, where it is not queued and the transaction is discarded. Any arguments after it are ignored.

## Reply

- `OK`, after which the server closes the connection.

## Examples

```
> SET q 1
OK
> QUIT
OK
```

A pipeline of `SET q 1`, `QUIT`, `SET q 2` gets `OK`, `OK` and a closed connection; `q` is `1`. Before authenticating:

```
> GET q
(error) NOAUTH Authentication required.
> QUIT
OK
```
