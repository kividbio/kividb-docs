---
title: "XINFO"
description: "Reports on a stream, its consumer groups and their consumers."
version: "1.2"
command: "XINFO"
syntax: "XINFO"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
subcommands: ["XINFO CONSUMERS", "XINFO GROUPS", "XINFO HELP", "XINFO STREAM"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XINFO
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`

Subcommands: [XINFO CONSUMERS](xinfo-consumers.md), [XINFO GROUPS](xinfo-groups.md), [XINFO HELP](xinfo-help.md), [XINFO STREAM](xinfo-stream.md)
<!-- generated: end -->
`XINFO` is a container: its subcommands report on a stream, its consumer groups, and their consumers. Use them to see how long a stream is, how far behind a group is, and which consumers hold unacknowledged entries.

| Subcommand | |
|---|---|
| [`XINFO STREAM`](xinfo-stream.md) | the stream's length, first and last entries, IDs and counters; `FULL` adds its groups and pending entries |
| [`XINFO GROUPS`](xinfo-groups.md) | each group's consumers, pending count, last delivered ID, entries read and lag |
| [`XINFO CONSUMERS`](xinfo-consumers.md) | each consumer of a group, its pending count, and how long since it was seen and since it was last given entries |
| [`XINFO HELP`](xinfo-help.md) | not implemented in 1.2.0 |

[`XPENDING`](xpending.md) lists the pending entries themselves, and [`XLEN`](xlen.md) is the quick way to the length alone.

`XINFO` needs a subcommand and a key: with fewer arguments it answers `ERR wrong number of arguments for 'xinfo' command`, whatever the subcommand, and a name that is not a subcommand gets `ERR unknown subcommand for XINFO`.

## Examples

```
> XINFO
(error) ERR wrong number of arguments for 'xinfo' command
> XINFO NOPE jobs
(error) ERR unknown subcommand for XINFO
> XINFO GROUPS jobs
1)  1) "name"
    2) "workers"
    3) "consumers"
    4) (integer) 2
    5) "pending"
    6) (integer) 3
    7) "last-delivered-id"
    8) "3-0"
    9) "entries-read"
   10) (integer) 3
   11) "lag"
   12) (integer) 0
```
