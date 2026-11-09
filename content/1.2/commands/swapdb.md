---
title: "SWAPDB"
description: "Swaps the contents of two databases in one step: every key, with its value and its time to live, moves from db1 to db2 and the other way round."
version: "1.2"
command: "SWAPDB"
syntax: "SWAPDB db1 db2"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["dangerous", "server", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SWAPDB db1 db2
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Swaps the contents of two databases in one step: every key, with its value and its time to live, moves from `db1` to `db2` and the other way round. Clients connected to either database see the other's keys from then on, without selecting anything. Use it to prepare a dataset in a spare database and then put it in place at once.

`db1` and `db2` are database numbers, from `0` to one less than the [`databases`](../reference/configuration.md#databases) setting (16 by default). Swapping a database with itself changes no data and replies `OK`, but like any `SWAPDB` it makes every [`WATCH`](watch.md) fail.

A client blocked on a key, by [`BLPOP`](blpop.md) for example, is woken if the swap brings it a value it can take. Every transaction that is [watching](watch.md) a key, in any database, fails at its `EXEC`, whether or not the key changed.

## Reply

- `OK`.
- `ERR invalid DB index` for a number that is not one of the databases.

## Examples

```
> SET greeting hello
OK
> SELECT 1
OK
> SET other 1
OK
> SELECT 0
OK
> SWAPDB 0 1
OK
> KEYS *
1) "other"
> SWAPDB 0 16
(error) ERR invalid DB index
```
