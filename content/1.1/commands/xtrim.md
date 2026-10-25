---
title: "XTRIM"
description: "Removes the oldest entries of the stream at key."
version: "1.1"
command: "XTRIM"
syntax: "XTRIM key MAXLEN|MINID [=|~] threshold [LIMIT count] [KEEPREF | DELREF | ACKED]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XTRIM key MAXLEN|MINID [=|~] threshold [LIMIT count] [KEEPREF | DELREF | ACKED]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Removes the oldest entries of the stream at `key`.

## Options

| Option | Effect |
|---|---|
| `MAXLEN n` | Keep the newest `n` entries. |
| `MINID id` | Remove the entries with IDs below `id`. |
| `~` | Trim approximately: whole nodes of `stream-node-max-entries` entries at a time, which is cheaper. `=` is exact (the default). |
| `LIMIT count` | With `~`, remove at most `count` entries. Without `~` it is an error, as in Redis. |
| `KEEPREF` | Leave consumer groups' pending references to removed entries (the default). |
| `DELREF` | Remove those references too. |
| `ACKED` | Stop at the first entry that some group has not acknowledged. |

## Reply

- The number of entries removed.

## Examples

```
> XADD u 1-0 a 1
"1-0"
> XADD u 2-0 a 2
"2-0"
> XADD u 3-0 a 3
"3-0"
> XTRIM u MAXLEN 1
(integer) 2
> XTRIM u MAXLEN 1 LIMIT 10
(error) ERR syntax error, LIMIT cannot be used without the special ~ option
```
