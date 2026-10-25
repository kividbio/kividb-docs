---
title: "PFDEBUG GETREG"
description: "Return an array of all 16384 register values (0–63) for the HyperLogLog at key; useful for inspecting which registers have been set and to what depth"
version: "1.1"
command: "PFDEBUG GETREG"
syntax: "PFDEBUG GETREG key"
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
PFDEBUG GETREG key
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return an array of all 16384 register values (0–63) for the HyperLogLog at `key`; useful for inspecting which registers have been set and to what depth
