---
title: "PFMERGE"
description: "Merges the HyperLogLogs at the source keys into destkey, so that it estimates their union."
version: "1.2"
command: "PFMERGE"
syntax: "PFMERGE destkey [sourcekey [sourcekey ...]]"
group: "hyperloglog"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["hyperloglog", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFMERGE destkey [sourcekey [sourcekey ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@hyperloglog`, `@slow`, `@write`
<!-- generated: end -->
Merges the HyperLogLogs at the source keys into `destkey`, so that it estimates their union. A missing source is empty.

The sources must be in the same hash space (see [`hll-write-format`](../reference/configuration.md#hll-write-format)). A new `destkey` takes theirs, or the setting's when there is no source.

## Reply

- `OK`.
- `ERR Cannot merge HyperLogLogs with different hash formats.` for sources of both hash spaces.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFADD h2 c d e f
(integer) 1
> PFMERGE m h h2
OK
> PFCOUNT m
(integer) 6
```
