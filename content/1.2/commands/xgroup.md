---
title: "XGROUP"
description: "XGROUP is a container: its subcommands create and manage consumer groups."
version: "1.2"
command: "XGROUP"
syntax: "XGROUP"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
subcommands: ["XGROUP CREATE", "XGROUP CREATECONSUMER", "XGROUP DELCONSUMER", "XGROUP DESTROY", "XGROUP HELP", "XGROUP SETID"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`

Subcommands: [XGROUP CREATE](xgroup-create.md), [XGROUP CREATECONSUMER](xgroup-createconsumer.md), [XGROUP DELCONSUMER](xgroup-delconsumer.md), [XGROUP DESTROY](xgroup-destroy.md), [XGROUP HELP](xgroup-help.md), [XGROUP SETID](xgroup-setid.md)
<!-- generated: end -->
`XGROUP` is a container: its subcommands create and manage consumer groups. A consumer group is a named reader of a stream that shares the stream's entries among its consumers, each entry going to one of them, and tracks which entries each consumer has been given and not yet acknowledged. It is how a stream is used as a work queue.

| Subcommand | |
|---|---|
| [`XGROUP CREATE`](xgroup-create.md) | create a group, reading from the start, the end, or an ID |
| [`XGROUP CREATECONSUMER`](xgroup-createconsumer.md) | add a consumer before it first reads |
| [`XGROUP DELCONSUMER`](xgroup-delconsumer.md) | remove a consumer and its pending entries |
| [`XGROUP SETID`](xgroup-setid.md) | move where the group reads from |
| [`XGROUP DESTROY`](xgroup-destroy.md) | delete a group |
| [`XGROUP HELP`](xgroup-help.md) | list the subcommands (since 1.2.1) |

Consumers read with [`XREADGROUP`](xreadgroup.md), acknowledge with [`XACK`](xack.md), and take over another's stalled entries with [`XCLAIM`](xclaim.md) or [`XAUTOCLAIM`](xautoclaim.md). [`XPENDING`](xpending.md) and [`XINFO GROUPS`](xinfo-groups.md) show what is outstanding.

`XGROUP` alone, or with a name that is not a subcommand, is an error. Since 1.2.1 the error for an unknown subcommand is Redis's, which names it and suggests `XGROUP HELP`; before, it was `ERR unknown subcommand for XGROUP`.

A subcommand on a key that does not exist gets Redis's error, `ERR The XGROUP subcommand requires the key to exist. Note that for CREATE you may want to use the MKSTREAM option to create an empty stream automatically.`; in 1.2.0, `XGROUP DESTROY` answered `0`. `XGROUP CREATE` takes `MKSTREAM` and `ENTRIESREAD` only after the ID, so a key or group called `mkstream` no longer creates the stream.

## Examples

```
> XGROUP
(error) ERR wrong number of arguments for 'xgroup' command
> XGROUP NOPE
(error) ERR unknown subcommand 'NOPE'. Try XGROUP HELP.
> XGROUP CREATE jobs workers 0
OK
```
