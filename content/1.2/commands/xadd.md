---
title: "XADD"
description: "Appends an entry, a set of field-value pairs, to the stream at key."
version: "1.2"
command: "XADD"
syntax: "XADD key [NOMKSTREAM] [KEEPREF | DELREF | ACKED] [IDMPAUTO producer-id | IDMP producer-id idempotent-id] [MAXLEN|MINID [=|~] threshold [LIMIT count]] *|id field value [...]"
group: "stream"
since: "1.1.0"
arity: -5
flags: ["fast", "write"]
acl_categories: ["fast", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XADD key [NOMKSTREAM] [KEEPREF | DELREF | ACKED] [IDMPAUTO producer-id | IDMP producer-id idempotent-id] [MAXLEN|MINID [=|~] threshold [LIMIT count]] *|id field value [...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@stream`, `@write`
<!-- generated: end -->
Appends an entry, a set of field-value pairs, to the stream at `key`. A missing key is created, unless `NOMKSTREAM` is given.

Every entry has an ID, `milliseconds-sequence`, and IDs only go up. `*` lets the server pick the ID from its clock; `ms-*` picks the next sequence for that millisecond; an explicit ID must be greater than the stream's last.

## Options

| Option | Effect |
|---|---|
| `NOMKSTREAM` | Do not create the stream if it does not exist. |
| `MAXLEN [=\|~] n`, `MINID [=\|~] id` | Then trim the stream as [`XTRIM`](xtrim.md) does. |
| `LIMIT count` | With `~`, remove at most `count` entries trimming. |
| `KEEPREF`, `DELREF`, `ACKED` | What trimming does with entries consumer groups still reference, as for [`XDELEX`](xdelex.md). |
| `IDMP producer-id idempotent-id` | Add the entry once: a retry with the same producer and idempotent ID adds nothing and replies with the first entry's ID (Redis 8.6). |
| `IDMPAUTO producer-id` | The same, with the entry's content as its idempotent ID. |

How long, and how many, idempotent IDs are remembered per producer is set by `stream-idmp-duration` and `stream-idmp-maxsize`, or per stream with [`XCFGSET`](xcfgset.md).

## Reply

- The entry's ID.
- `nil` with `NOMKSTREAM` when the key does not exist.
- `ERR The ID specified in XADD is equal or smaller than the target stream top item` for an ID that is not greater than the last.

## Examples

```
> XADD s 1-1 temp 20
"1-1"
> XADD s 2-0 temp 22 hum 50
"2-0"
> XADD s 3-* temp 23
"3-0"
> XADD s 1-5 temp 1
(error) ERR The ID specified in XADD is equal or smaller than the target stream top item
> XADD i IDMP p1 req-1 * amount 10
"1792966338089-0"
> XADD i IDMP p1 req-1 * amount 10
"1792966338089-0"
> XLEN i
(integer) 1
```
