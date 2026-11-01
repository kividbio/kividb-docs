---
title: "PFDEBUG DECODE"
description: "Returns the runs of a sparse HyperLogLog, as Redis does: Z:n for n zero registers, v:value,count for count registers holding value."
version: "1.2"
command: "PFDEBUG DECODE"
syntax: "PFDEBUG DECODE key"
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
PFDEBUG DECODE key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the runs of a sparse HyperLogLog, as Redis does: `Z:n` for `n` zero registers, `v:value,count` for `count` registers holding `value`. A dense one is refused with `ERR HLL encoding is not sparse`; KiviDB writes only dense ones, so this is for HyperLogLogs that came from Redis.

## Examples

```
> PFDEBUG DECODE h
"v:2,1 Z:16383"
```

Before 1.2, it returned a summary of a dense HyperLogLog (`encoding:dense registers:16384 nonzero:4 …`).
