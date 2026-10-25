---
title: "XDELEX"
description: "Deletes entries from the stream at key, with control over the references consumer groups hold to them (Redis 8.2)."
version: "1.1"
command: "XDELEX"
syntax: "XDELEX key [KEEPREF | DELREF | ACKED] IDS numids id [id ...]"
group: "stream"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XDELEX key [KEEPREF | DELREF | ACKED] IDS numids id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Deletes entries from the stream at `key`, with control over the references consumer groups hold to them (Redis 8.2). `numids` is how many IDs follow `IDS`. The policy can also come after the IDs.

| Policy | Effect |
|---|---|
| `KEEPREF` | Delete, and leave groups' pending references (the default). |
| `DELREF` | Delete, and remove the entry from every group's pending list. |
| `ACKED` | Delete only an entry every group has read and acknowledged. `REF` is accepted as an older name. |

## Reply

An array with one element per ID:
- `1`: deleted;
- `2`: kept, because a group still references it (`ACKED` only);
- `-1`: no such entry.

## Examples

```
> XADD q 3-0 t c
"3-0"
> XGROUP CREATE q g 0
OK
> XREADGROUP GROUP g c1 STREAMS q >
1) 1) "q"
   2) 1) 1) "3-0"
         2) 1) "t"
            2) "c"
> XDELEX q ACKED IDS 1 3-0
1) (integer) 2
> XDELEX q DELREF IDS 2 3-0 9-0
1) (integer) 1
2) (integer) -1
```
