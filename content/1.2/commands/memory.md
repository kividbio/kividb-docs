---
title: "MEMORY"
description: "MEMORY is a container: its subcommands report on the server's memory and on what a key takes."
version: "1.2"
command: "MEMORY"
syntax: "MEMORY"
group: "server"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["server", "slow"]
history: []
subcommands: ["MEMORY DOCTOR", "MEMORY HELP", "MEMORY MALLOC-STATS", "MEMORY PURGE", "MEMORY STATS", "MEMORY USAGE"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MEMORY
```

**Available since:** 1.1.0 · **ACL categories:** `@server`, `@slow`

Subcommands: [MEMORY DOCTOR](memory-doctor.md), [MEMORY HELP](memory-help.md), [MEMORY MALLOC-STATS](memory-malloc-stats.md), [MEMORY PURGE](memory-purge.md), [MEMORY STATS](memory-stats.md), [MEMORY USAGE](memory-usage.md)
<!-- generated: end -->
`MEMORY` is a container: its subcommands report on the server's memory and on what a key takes.

| Subcommand | |
|---|---|
| [`MEMORY USAGE`](memory-usage.md) | the bytes a key and its value take |
| [`MEMORY STATS`](memory-stats.md) | the server's memory figures, as name-value pairs |
| [`MEMORY DOCTOR`](memory-doctor.md) | a sentence on anything that looks wrong |
| [`MEMORY PURGE`](memory-purge.md) | ask the allocator to give free memory back |
| [`MEMORY MALLOC-STATS`](memory-malloc-stats.md) | the allocator's own report, which KiviDB does not have |
| [`MEMORY HELP`](memory-help.md) | the list, from the server |

[Memory](../guides/memory.md) explains what a key takes, how memory is counted, and what deleting gives back. `MEMORY` alone is an error.

## Examples

```
> MEMORY
(error) ERR wrong number of arguments for 'memory' command
> HSET user:1 name Alice
(integer) 1
> MEMORY USAGE user:1
(integer) 193
```
