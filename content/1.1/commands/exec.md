---
title: "EXEC"
description: "Runs the commands queued since MULTI, as one step: no other client's command that could see their keys starts between two of them, reads included, so nobody sees the transaction half done."
version: "1.1"
command: "EXEC"
syntax: "EXEC"
group: "transaction"
since: "1.1.0"
arity: 1
flags: []
acl_categories: ["slow", "transaction"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
EXEC
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@transaction`
<!-- generated: end -->
Runs the commands queued since [`MULTI`](multi.md), as one step: no other client's command that could see their keys starts between two of them, reads included, so nobody sees the transaction half done.

A command that fails while running does not stop the others: its error is its element of the reply. A command refused while queueing (an unknown command, a wrong number of arguments) makes `EXEC` run nothing.

If a key [`WATCH`](watch.md)ed before `MULTI` was changed by anyone since, `EXEC` runs nothing.

## Reply

- An array with each queued command's reply.
- `nil` if a watched key had changed.
- `EXECABORT Transaction discarded because of previous errors.` if a command was refused while queueing.
- `ERR EXEC without MULTI` outside a transaction.

## Examples

```
> MULTI
OK
> SET k v
QUEUED
> INCR k
QUEUED
> SET k2 v2
QUEUED
> EXEC
1) OK
2) (error) ERR value is not an integer or out of range
3) OK
```

A queueing error:

```
> MULTI
OK
> NOSUCHCMD
(error) ERR unknown command 'NOSUCHCMD', with args beginning with:
> EXEC
(error) EXECABORT Transaction discarded because of previous errors.
```
