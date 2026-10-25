---
title: "PFDEBUG DECODE"
description: "Returns a summary of the HyperLogLog: its encoding, how many of its 16,384 registers are not zero, the largest register, and its estimate."
version: "1.1"
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
Returns a summary of the HyperLogLog: its encoding, how many of its 16,384 registers are not zero, the largest register, and its estimate.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFDEBUG DECODE h
"encoding:dense registers:16384 nonzero:4 max_register:2 estimate:4"
```
