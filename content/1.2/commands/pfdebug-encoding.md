---
title: "PFDEBUG ENCODING"
description: "Returns how the HyperLogLog at key is stored: dense, the full 16,384 registers, or sparse, Redis's compact form for one with few elements."
version: "1.2"
command: "PFDEBUG ENCODING"
syntax: "PFDEBUG ENCODING key"
group: "hyperloglog"
since: "1.1.0"
history: []
container: "PFDEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFDEBUG ENCODING key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how the HyperLogLog at `key` is stored: `dense`, the full 16,384 registers, or `sparse`, Redis's compact form for one with few elements. KiviDB writes only dense ones, so `sparse` means a value Redis wrote, from a snapshot or a [`RESTORE`](restore.md), that has not been written to since. Use it when checking what a migration from Redis brought over.

A sparse HyperLogLog is read as it is, and becomes dense on its first write: [`PFADD`](pfadd.md), [`PFDEBUG RESET`](pfdebug-reset.md) or [`PFDEBUG TODENSE`](pfdebug-todense.md). Reading it with [`PFCOUNT`](pfcount.md) or [`PFDEBUG GETREG`](pfdebug-getreg.md) leaves it sparse. `PFDEBUG ENCODING` changes nothing.

## Reply

- `dense` or `sparse`, as a simple string.
- `ERR The specified key does not exist` if the key is missing.
- `WRONGTYPE Key is not a valid HyperLogLog string value.` if the key holds something else.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFDEBUG ENCODING h
dense
> PFDEBUG ENCODING nosuch
(error) ERR The specified key does not exist
> SET a 1
OK
> PFDEBUG ENCODING a
(error) WRONGTYPE Key is not a valid HyperLogLog string value.
```
