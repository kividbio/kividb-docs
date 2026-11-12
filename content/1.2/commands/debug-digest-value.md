---
title: "DEBUG DIGEST-VALUE"
description: "For each key, a digest of its value in 40 hexadecimal digits, or 40 zeros for a key that is not there, as in Redis."
version: "1.2"
command: "DEBUG DIGEST-VALUE"
syntax: "DEBUG DIGEST-VALUE key [key ...]"
group: "server"
since: "1.2.1"
history: []
container: "DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG DIGEST-VALUE key [key ...]
```

**Available since:** 1.2.1
<!-- generated: end -->
For each key, a digest of its value in 40 hexadecimal digits, or 40 zeros for a key that is not there, as in Redis. Two keys with the same value of the same type have the same digest, whatever their names. `redis-cli --cluster fix` compares the copies of a key it finds on two nodes with it.

`COMMAND` lists the `DEBUG` subcommands since 1.2.1, so each has a page; `DEBUG DIGEST-VALUE` itself is since 1.2.0, when it replaced an `OK` that did nothing. Since 1.2.1 it takes a key of any bytes. See [`DEBUG`](debug.md).

## Reply

An array of digests, one for each key, in the order given.

## Examples

```
> SET k v
OK
> DEBUG DIGEST-VALUE k nokey
1) "00000000bf043f6d6fecb329f8d67d15e882c12b"
2) "0000000000000000000000000000000000000000"
```
