---
title: "XACKDEL"
description: "Acknowledges entries for the group and deletes them from the stream, in one step (Redis 8.2)."
version: "1.2"
command: "XACKDEL"
syntax: "XACKDEL key group [KEEPREF | DELREF | ACKED] IDS numids id [id ...]"
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
XACKDEL key group [KEEPREF | DELREF | ACKED] IDS numids id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Acknowledges entries for the group and deletes them from the stream, in one step (Redis 8.2). `numids` is how many IDs follow `IDS`. The policy, `KEEPREF` (the default), `DELREF` or `ACKED`, is as for [`XDELEX`](xdelex.md). The older form `XACKDEL key group id [id ...]` is still accepted.

## Reply

An array with one element per ID:
- `1`: acknowledged and deleted, or already gone;
- `2`: acknowledged, but kept because another group still references it (`ACKED` only);
- `-1`: not pending in this group.

## Examples

```
> XADD q 1-0 t a
"1-0"
> XADD q 2-0 t b
"2-0"
> XGROUP CREATE q g1 0
OK
> XGROUP CREATE q g2 0
OK
> XREADGROUP GROUP g1 c1 STREAMS q >
...
> XREADGROUP GROUP g2 c1 COUNT 1 STREAMS q >
...
> XACKDEL q g1 ACKED IDS 2 1-0 2-0
1) (integer) 2
2) (integer) 2
> XACKDEL q g2 IDS 1 1-0
1) (integer) 1
```
