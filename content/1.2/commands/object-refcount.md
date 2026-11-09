---
title: "OBJECT REFCOUNT"
description: "Returns how many references there are to the value stored at key."
version: "1.2"
command: "OBJECT REFCOUNT"
syntax: "OBJECT REFCOUNT key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
OBJECT REFCOUNT key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many references there are to the value stored at `key`. KiviDB never shares one value between several keys, so for a key that exists the answer is always `1`, whatever its type and size. The command is there for clients and tools that call it.

To learn something real about a key's value, use [`OBJECT ENCODING`](object-encoding.md), [`MEMORY USAGE`](memory-usage.md) or [`TYPE`](type.md).

## Reply

- `1` if the key exists.
- `nil` if it does not.

## Examples

```
> SET a 123
OK
> OBJECT REFCOUNT a
(integer) 1
> RPUSH l x
(integer) 1
> OBJECT REFCOUNT l
(integer) 1
> OBJECT REFCOUNT missing
(nil)
```
