---
title: "PFDEBUG RESET"
description: "Sets every register of the HyperLogLog to zero, so that it counts 0; the key is kept."
version: "1.1"
command: "PFDEBUG RESET"
syntax: "PFDEBUG RESET key"
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
PFDEBUG RESET key
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets every register of the HyperLogLog to zero, so that it counts 0; the key is kept.

## Examples

```
> PFDEBUG RESET h
OK
> PFCOUNT h
(integer) 0
```
