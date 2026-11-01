---
title: "DEBUG"
description: "For tests and tools written for Redis."
version: "1.2"
command: "DEBUG"
syntax: "DEBUG ..."
group: "server"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG ...
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
For tests and tools written for Redis. The subcommands that do something:

- `DEBUG SLEEP seconds`: the thread that runs it sleeps that long, which holds up the clients that share it; useful for testing timeouts.
- `DEBUG POPULATE count [prefix] [size]`: makes `count` string keys, `prefix:0` onwards (`key:0` without a prefix), holding `value:0` onwards, cut or padded with zero bytes to `size` bytes when one is given. A key that is there already is left as it is. Before 1.2, it replied `OK` and made nothing.
- `DEBUG PROTOCOL type`: replies with a value of that type (`string`, `integer`, `double`, `bignum`, `null`, `array`, `set`, `map`, ...), for testing a client's RESP3 support.

`DEBUG OBJECT` replies with a fixed line, not the key's. Every other subcommand replies `OK` and does nothing.

## Examples

```
> DEBUG POPULATE 2
OK
> GET key:0
"value:0"
> DEBUG POPULATE 1 p 12
OK
> STRLEN p:0
(integer) 12
```
