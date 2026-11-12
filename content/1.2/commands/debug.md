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
acl_categories: ["admin", "dangerous", "slow"]
history: [{"release": "1.2.1", "change": "acl categories: removed server"}]
subcommands: ["DEBUG DIGEST-VALUE", "DEBUG HELP", "DEBUG LOG", "DEBUG OBJECT", "DEBUG PAUSE-CRON", "DEBUG POPULATE", "DEBUG PROTOCOL", "DEBUG SET-ACTIVE-EXPIRE", "DEBUG SET-DISABLE-DENY-SCRIPTS", "DEBUG SLEEP"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG ...
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@slow`

Subcommands: [DEBUG DIGEST-VALUE](debug-digest-value.md), [DEBUG HELP](debug-help.md), [DEBUG LOG](debug-log.md), [DEBUG OBJECT](debug-object.md), [DEBUG PAUSE-CRON](debug-pause-cron.md), [DEBUG POPULATE](debug-populate.md), [DEBUG PROTOCOL](debug-protocol.md), [DEBUG SET-ACTIVE-EXPIRE](debug-set-active-expire.md), [DEBUG SET-DISABLE-DENY-SCRIPTS](debug-set-disable-deny-scripts.md), [DEBUG SLEEP](debug-sleep.md)

**History:**

- 1.2.1: acl categories: removed server
<!-- generated: end -->
For tests and tools written for Redis. The subcommands, each with a page of its own:

- [`DEBUG SLEEP seconds`](debug-sleep.md): the thread that runs it sleeps that long, which holds up the clients that share it; useful for testing timeouts.
- [`DEBUG POPULATE count [prefix] [size]`](debug-populate.md): makes `count` string keys, `prefix:0` onwards (`key:0` without a prefix), holding `value:0` onwards, cut or padded with zero bytes to `size` bytes when one is given. A key that is there already is left as it is. Before 1.2, it replied `OK` and made nothing.
- [`DEBUG PROTOCOL type`](debug-protocol.md): replies with a value of that type (`string`, `integer`, `double`, `bignum`, `null`, `array`, `set`, `map`, ...), for testing a client's RESP3 support.
- [`DEBUG DIGEST-VALUE key [key ...]`](debug-digest-value.md): for each key, a digest of its value in 40 hex digits, or 40 zeros for a key that is not there, as in Redis. `redis-cli --cluster fix` compares the copies of a key it finds on two nodes with it. New in 1.2; before, it replied `OK`.
- [`DEBUG OBJECT key`](debug-object.md): the key's encoding, serialized length and last use, in Redis's form.
- [`DEBUG LOG message`](debug-log.md): writes `message` to the server's log.
- [`DEBUG PAUSE-CRON 0|1`](debug-pause-cron.md) and [`DEBUG SET-ACTIVE-EXPIRE 0|1`](debug-set-active-expire.md): pause and resume the background expiry.
- [`DEBUG SET-DISABLE-DENY-SCRIPTS 0|1`](debug-set-disable-deny-scripts.md): accepted, and changes nothing.
- [`DEBUG HELP`](debug-help.md): lists them.

Any other subcommand, Redis's `RELOAD`, `LOADAOF` and `CHANGE-REPL-ID` among them, or one with the wrong number of arguments, is refused with Redis's `ERR unknown subcommand or wrong number of arguments for '<name>'. Try DEBUG HELP.`.

Since 1.2.1. In 1.2.0, `DEBUG OBJECT` replied with a fixed line, whatever the key, and every other subcommand, `HELP`, `LOG`, `PAUSE-CRON`, `SET-ACTIVE-EXPIRE` and `RELOAD` among them, replied `OK` and did nothing. A test suite that relied on `DEBUG RELOAD` replying `OK` now gets the error.

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
