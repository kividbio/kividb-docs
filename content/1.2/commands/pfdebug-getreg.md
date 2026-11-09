---
title: "PFDEBUG GETREG"
description: "Returns all 16,384 registers of the HyperLogLog, each from 0 to 63, dense or sparse."
version: "1.2"
command: "PFDEBUG GETREG"
syntax: "PFDEBUG GETREG key"
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
PFDEBUG GETREG key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns all 16,384 registers of the HyperLogLog at `key`, in order, each a number from 0 to 63. Each element added picks one register by its hash, and raises it to a value taken from the rest of the hash if that is higher; [`PFCOUNT`](pfcount.md) estimates from them all. Use it to debug, or to compare a HyperLogLog with another, register by register.

Which register an element sets depends on the hash space the HyperLogLog was made in ([`hll-write-format`](../reference/configuration.md#hll-write-format)): KiviDB's own, the default, or Redis's.

A sparse HyperLogLog, one Redis wrote, is read as it is and stays sparse: `GETREG` does not change the value, where Redis's converts it to dense first.

## Reply

- An array of 16,384 integers.
- `ERR The specified key does not exist` if the key is missing.
- `WRONGTYPE Key is not a valid HyperLogLog string value.` if the key holds something else.

## Examples

```
> PFADD h2 x y
(integer) 1
> PFDEBUG GETREG h2
    1) (integer) 0
    2) (integer) 0
...
  426) (integer) 3
...
15669) (integer) 2
...
16384) (integer) 0
> PFDEBUG GETREG nosuch
(error) ERR The specified key does not exist
```
