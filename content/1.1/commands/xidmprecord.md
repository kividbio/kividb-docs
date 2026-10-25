---
title: "XIDMPRECORD"
description: "Records that producer producer-id's idempotent ID idempotent-id produced the entry id, already in the stream at key, as an XADD ..."
version: "1.1"
command: "XIDMPRECORD"
syntax: "XIDMPRECORD"
group: "other"
since: "1.1.1"
arity: 5
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XIDMPRECORD
```

**Available since:** 1.1.1 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Records that producer `producer-id`'s idempotent ID `idempotent-id` produced the entry `id`, already in the stream at `key`, as an `XADD ... IDMP` would have (Redis 8.10). A later `XADD` with that producer and idempotent ID then adds nothing and replies with `id`. Recording the same pair again is fine.

## Reply

- `OK`.
- `ERR No such message in stream` if there is no entry `id`; `ERR no such key` if the stream does not exist.

## Examples

```
> XADD r 1-0 x 1
"1-0"
> XIDMPRECORD r p1 req-9 1-0
OK
> XADD r IDMP p1 req-9 * x 2
"1-0"
> XLEN r
(integer) 1
```
