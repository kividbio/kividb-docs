---
title: "XLEN"
description: "Returns the number of entries in the stream at key."
version: "1.2"
command: "XLEN"
syntax: "XLEN key"
group: "stream"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "stream"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XLEN key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@stream`
<!-- generated: end -->
Returns the number of entries in the stream at `key`. It counts the entries the stream holds now: those removed by [`XDEL`](xdel.md) or [`XTRIM`](xtrim.md) are not counted. [`XINFO STREAM`](xinfo-stream.md) reports `entries-added`, how many the stream has ever had.

A stream whose entries have all been deleted still exists, with a length of `0`, unlike a list, which is deleted with its last element. That keeps its consumer groups and last ID.

## Reply

- The number of entries; `0` if the key does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> XADD s 1-0 a 1
"1-0"
> XADD s 2-0 a 2
"2-0"
> XLEN s
(integer) 2
> XDEL s 1-0 2-0
(integer) 2
> XLEN s
(integer) 0
> EXISTS s
(integer) 1
> XLEN nokey
(integer) 0
```
