---
title: "PFADD"
description: "Adds elements to the HyperLogLog at key: a structure of fixed size that estimates how many different elements it has been given, however many that is."
version: "1.2"
command: "PFADD"
syntax: "PFADD key [element [element ...]]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "hyperloglog", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFADD key [element [element ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hyperloglog`, `@write`
<!-- generated: end -->
Adds elements to the HyperLogLog at `key`: a structure of fixed size that estimates how many different elements it has been given, however many that is. With its 16,384 registers, as in Redis, the estimate's standard error is about 0.81%. A missing key is created, even with no elements.

KiviDB writes every HyperLogLog dense, 12,304 bytes. A new one is made in the hash space [`hll-write-format`](../reference/configuration.md#hll-write-format) names: `legacy`, the default, KiviDB's own, or `redis`, Redis's (MurmurHash64A), which a Redis server reads the same. An existing one keeps the hash space it was made in. A HyperLogLog Redis wrote sparse, from a snapshot or a `RESTORE`, is read, and `PFADD` rewrites it dense.

## Reply

- `1` if the HyperLogLog changed (its estimate may have), `0` if not.
- `WRONGTYPE Key is not a valid HyperLogLog string value.` if the key holds a string that is not a HyperLogLog.
- `INVALIDOBJ Corrupted HLL object detected` if it holds a sparse HyperLogLog that cannot be read.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFADD h a
(integer) 0
> PFCOUNT h
(integer) 4
```

Before 1.2, every HyperLogLog was in KiviDB's own hash space, and a sparse one from Redis was `WRONGTYPE`.
