---
title: "OBJECT"
description: "OBJECT is a container: its subcommands report on a single key's value, and on how the key has been used."
version: "1.2"
command: "OBJECT"
syntax: "OBJECT"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
subcommands: ["OBJECT ENCODING", "OBJECT FREQ", "OBJECT HELP", "OBJECT IDLETIME", "OBJECT REFCOUNT"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
OBJECT
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`

Subcommands: [OBJECT ENCODING](object-encoding.md), [OBJECT FREQ](object-freq.md), [OBJECT HELP](object-help.md), [OBJECT IDLETIME](object-idletime.md), [OBJECT REFCOUNT](object-refcount.md)
<!-- generated: end -->
`OBJECT` is a container: its subcommands report on a single key's value, and on how the key has been used.

| Subcommand | |
|---|---|
| [`OBJECT ENCODING`](object-encoding.md) | the encoding Redis would use for the value; KiviDB keeps each type one way |
| [`OBJECT IDLETIME`](object-idletime.md) | seconds since the key was last used, kept under an LRU or LRM `maxmemory-policy` |
| [`OBJECT FREQ`](object-freq.md) | the key's use count, kept under an LFU `maxmemory-policy` |
| [`OBJECT REFCOUNT`](object-refcount.md) | always `1`: values are not shared between keys |
| [`OBJECT HELP`](object-help.md) | the list, from the server |

[Memory](../guides/memory.md) explains how use is counted for eviction, and why encodings are only names in KiviDB. `OBJECT` does not count as a use of the key. For a missing key, each subcommand returns `nil`.

`OBJECT` alone, or with a name that is not one of these, is an error.

## Examples

```
> OBJECT
(error) ERR wrong number of arguments for 'object' command
> OBJECT NOPE
(error) ERR unknown subcommand
> SET a 123
OK
> OBJECT ENCODING a
"int"
> OBJECT ENCODING missing
(nil)
```
