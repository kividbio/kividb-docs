---
title: "DEBUG OBJECT"
description: "Describes the value at key in Redis's form: its encoding, the length of its serialized form and when it was last used."
version: "1.2"
command: "DEBUG OBJECT"
syntax: "DEBUG OBJECT key"
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
DEBUG OBJECT key
```

**Available since:** 1.2.1
<!-- generated: end -->
Describes the value at `key` in Redis's form: its encoding, the length of its serialized form and when it was last used. Tools and tests written for Redis read it, mostly for the `encoding`; [`OBJECT ENCODING`](object-encoding.md) gives that alone.

- `Value at` is always `0x0`, and `refcount` `1`.
- `encoding` is the one [`OBJECT ENCODING`](object-encoding.md) gives: `embstr`, `int`, `listpack` and the rest.
- `serializedlength` is the length of the key's [`DUMP`](dump.md) payload, not of Redis's RDB form.
- `lru` and `lru_seconds_idle` are `0` unless an LRU or LFU eviction policy, or [`key-access-tracking`](../reference/configuration.md#key-access-tracking), is on.

A key past its time is shown while it is still there, and looking at it is not a use. Since 1.2.1; in 1.2.0 it replied with a fixed line, whatever the key. See [`DEBUG`](debug.md).

## Reply

- The description, as a simple string.
- `ERR no such key`.

## Examples

```
> RPUSH l a b c
(integer) 3
> DEBUG OBJECT l
Value at:0x0 refcount:1 encoding:listpack serializedlength:19 lru:0 lru_seconds_idle:0
> DEBUG OBJECT nokey
(error) ERR no such key
```
