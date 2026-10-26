---
title: "DUMP"
description: "Serializes the value at key into a payload that RESTORE turns back into the value."
version: "1.1"
command: "DUMP"
syntax: "DUMP key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["readonly"]
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DUMP key
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Serializes the value at `key` into a payload that [`RESTORE`](restore.md) turns back into the value.

The payload is in KiviDB's own snapshot format, with a 2-byte version and a CRC64 checksum at the end, as Redis does. It restores into KiviDB, not into Redis. Time series and vector sets, which Redis has no type for, dump and restore between KiviDB servers.

## Reply

- The payload, as a bulk string.
- `nil` if the key does not exist.

## Examples

```
> SET src hello
OK
> DUMP src
"\x01\x05\x00\x00\x00hello\n\x00..."
```
