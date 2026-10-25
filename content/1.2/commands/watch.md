---
title: "WATCH"
description: "Watches keys for the next transaction on this connection: if any of them is changed, by any client, before EXEC, the transaction runs nothing and EXEC replies nil."
version: "1.2"
command: "WATCH"
syntax: "WATCH key [key ...]"
group: "transaction"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "transaction"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
WATCH key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
Watches keys for the next transaction on this connection: if any of them is changed, by any client, before [`EXEC`](exec.md), the transaction runs nothing and `EXEC` replies `nil`. This is optimistic locking: read, decide, and write only if nothing changed meanwhile, or try again.

Of two transactions racing on a watched key, the second always sees the first's write. Keys stop being watched at `EXEC`, `DISCARD` or [`UNWATCH`](unwatch.md).

## Reply

- `OK`.
- `ERR WATCH inside MULTI is not allowed`.

## Examples

```
client 1> SET bal 100
OK
client 1> WATCH bal
OK
client 1> MULTI
OK
client 1> DECRBY bal 10
QUEUED
client 2> SET bal 50
OK
client 1> EXEC
(nil)
client 1> GET bal
"50"
```
