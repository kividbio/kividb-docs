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
Returns all 16,384 registers of the HyperLogLog, each from 0 to 63, dense or sparse. It does not change the value.

`ERR The specified key does not exist` if the key is missing.
