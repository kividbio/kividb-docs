---
title: "PFDEBUG RESET"
description: "Zero all registers and invalidate the cached cardinality, effectively resetting the HyperLogLog to empty while keeping the key; AOF-logged"
version: "1.1"
command: "PFDEBUG RESET"
syntax: "PFDEBUG RESET key"
group: "hyperloglog"
since: "1.1.0"
history: []
container: "PFDEBUG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PFDEBUG RESET key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Zero all registers and invalidate the cached cardinality, effectively resetting the HyperLogLog to empty while keeping the key; AOF-logged
