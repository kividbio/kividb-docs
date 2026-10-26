---
title: "BITFIELD_RO"
description: "BITFIELD with GET only: it only reads, so it can be sent to a read-only replica."
version: "1.2"
command: "BITFIELD_RO"
syntax: "BITFIELD_RO key [GET encoding offset [GET encoding offset ...]]"
group: "bitmap"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["bitmap", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BITFIELD_RO key [GET encoding offset [GET encoding offset ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@read`, `@slow`
<!-- generated: end -->
[`BITFIELD`](bitfield.md) with `GET` only: it only reads, so it can be sent to a read-only replica.

## Reply

- An array with one element per `GET`.
- `ERR BITFIELD_RO only supports the GET subcommand` for anything else.

## Examples

```
> BITFIELD bf SET u8 0 244
1) (integer) 0
> BITFIELD_RO bf GET u8 0
1) (integer) 244
```
