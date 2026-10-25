---
title: "XNACK"
description: "Releases pending entries back to the group without acknowledging them, so that another consumer can take them at once, with XREADGROUP ..."
version: "1.2"
command: "XNACK"
syntax: "XNACK key group <SILENT | FAIL | FATAL> IDS numids id [id ...] [RETRYCOUNT count] [FORCE]"
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
XNACK key group <SILENT | FAIL | FATAL> IDS numids id [id ...] [RETRYCOUNT count] [FORCE]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Releases pending entries back to the group without acknowledging them, so that another consumer can take them at once, with [`XREADGROUP ... CLAIM`](xreadgroup.md) or [`XAUTOCLAIM`](xautoclaim.md). A released entry has no owner. `numids` is how many IDs follow `IDS`.

| Mode | Delivery count |
|---|---|
| `SILENT` | lowered by one, as if this delivery had not happened |
| `FAIL` | left as it is |
| `FATAL` | set to the maximum, marking the entry as one that keeps failing |

`RETRYCOUNT count` sets the delivery count instead. `FORCE` also makes entries that exist in the stream but are not pending into unowned pending ones.

## Reply

- The number of entries released.

## Examples

```
> XADD n 1-0 t a
"1-0"
> XGROUP CREATE n g 0
OK
> XREADGROUP GROUP g w STREAMS n >
...
> XNACK n g FAIL IDS 1 1-0
(integer) 1
> XREADGROUP GROUP g w2 CLAIM 0 STREAMS n >
1) 1) "n"
   2) 1) 1) "1-0"
         2) 1) "t"
            2) "a"
         3) (integer) 0
         4) (integer) 1
```
