---
title: "PFDEBUG RESET"
description: "Sets every register of the HyperLogLog at key to zero, so that PFCOUNT gives 0 and it counts again from nothing."
version: "1.2"
command: "PFDEBUG RESET"
syntax: "PFDEBUG RESET key"
group: "hyperloglog"
since: "1.1.0"
history: []
container: "PFDEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFDEBUG RESET key
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets every register of the HyperLogLog at `key` to zero, so that [`PFCOUNT`](pfcount.md) gives `0` and it counts again from nothing. The key stays, with its time to live; a sparse one, from Redis, is written back dense. Use it to empty a HyperLogLog in place, for tests or debugging; [`DEL`](del.md) does the same for counting, by removing the key.

It is a write: it reaches replicas and the append-only file like any other ([`PFDEBUG`](pfdebug.md)).

## Reply

- `OK`.
- `ERR The specified key does not exist` if the key is missing.
- `WRONGTYPE Key is not a valid HyperLogLog string value.` if the key holds something else.

## Examples

```
> PFADD t a b c
(integer) 1
> EXPIRE t 100
(integer) 1
> PFDEBUG RESET t
OK
> PFCOUNT t
(integer) 0
> TTL t
(integer) 100
> PFADD t a
(integer) 1
> PFCOUNT t
(integer) 1
> PFDEBUG RESET nosuch
(error) ERR The specified key does not exist
```
