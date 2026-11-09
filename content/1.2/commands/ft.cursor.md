---
title: "FT.CURSOR"
description: "FT.CURSOR is a container: its subcommands read and close the cursors that FT.AGGREGATE ... WITHCURSOR opens, so that a large aggregation can be read a page at a time instead of in one reply."
version: "1.2"
command: "FT.CURSOR"
syntax: "FT.CURSOR"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
subcommands: ["FT.CURSOR DEL", "FT.CURSOR READ"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CURSOR
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`

Subcommands: [FT.CURSOR DEL](ft.cursor-del.md), [FT.CURSOR READ](ft.cursor-read.md)
<!-- generated: end -->
`FT.CURSOR` is a container: its subcommands read and close the cursors that [`FT.AGGREGATE ... WITHCURSOR`](ft.aggregate.md) opens, so that a large aggregation can be read a page at a time instead of in one reply.

| Subcommand | |
|---|---|
| [`FT.CURSOR READ`](ft.cursor-read.md) | the next rows, and the cursor to read on with (`0` at the end) |
| [`FT.CURSOR DEL`](ft.cursor-del.md) | close a cursor before it is read to the end |
| `FT.CURSOR GC` | drop the cursors left unread longer than they may be, and return how many |

A cursor holds the rows the aggregation produced when it ran. It is closed when it is read to the end, deleted, left unread longer than its `MAXIDLE` (at most `CURSOR_MAX_IDLE`, 300000 ms by default; see [`FT.CONFIG`](ft.config.md)), or when its index is dropped. Idle cursors are dropped whenever any cursor is used, so `FT.CURSOR GC` is seldom needed. At most 1024 cursors can be open at once; past that, `FT.AGGREGATE ... WITHCURSOR` fails with `Too many cursors allocated for index`. In a [cluster](../guides/cluster.md), the cursor is kept on the node the aggregation was sent to.

Name the index the cursor was opened on, by its own name: an alias is not accepted.

## Examples

```
> FT.CURSOR
(error) ERR wrong number of arguments for 'FT.CURSOR' command
> FT.CURSOR NOPE
(error) Unknown subcommand
> FT.CURSOR GC products
(integer) 0
```
