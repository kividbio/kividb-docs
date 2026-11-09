---
title: "CLIENT ID"
description: "Returns the connection's ID, unique for the server's lifetime."
version: "1.2"
command: "CLIENT ID"
syntax: "CLIENT ID"
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
CLIENT ID
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the connection's ID. IDs start at 1 when the server starts and only go up, so an ID is never given to a second connection while the server runs, and a higher ID means a later connection.

The ID is what other commands take to name a connection: [`CLIENT KILL ID`](client-kill.md), [`CLIENT UNBLOCK`](client-unblock.md), `REDIRECT` in [`CLIENT TRACKING`](client-tracking.md), and `CLIENT LIST ID`. It is the `id=` field of [`CLIENT LIST`](client-list.md).

## Reply

The ID, as an integer.

## Examples

```
> CLIENT ID
(integer) 7
> CLIENT LIST ID 7
"id=7 addr=127.0.0.1:45906 ... cmd=client|list user=default ..."
```
