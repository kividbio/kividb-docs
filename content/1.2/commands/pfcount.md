---
title: "PFCOUNT"
description: "Returns the estimated number of different elements added to the HyperLogLog at key."
version: "1.2"
command: "PFCOUNT"
syntax: "PFCOUNT key [key ...]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["hyperloglog", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFCOUNT key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hyperloglog`, `@read`, `@slow`
<!-- generated: end -->
Returns the estimated number of different elements added to the HyperLogLog at `key`. With several keys, the estimate for their union, without storing it.

The estimate is Ertl's, as in Redis, for both hash spaces. Several keys must be in the same hash space (see [`hll-write-format`](../reference/configuration.md#hll-write-format)): a mixture is refused rather than estimated.

## Reply

- The estimate; `0` if the key does not exist.
- `ERR Cannot PFCOUNT HyperLogLogs with different hash formats.` for keys of both hash spaces.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFADD h2 c d e f
(integer) 1
> PFCOUNT h h2
(integer) 6
```

In 1.2 the estimator is Ertl's for HyperLogLogs in KiviDB's own hash space too, so an estimate can differ slightly from 1.1's for the same key.
