---
title: "PFDEBUG ENCODING"
description: "Returns the HyperLogLog's encoding: always dense in KiviDB, which does not use Redis's sparse encoding."
version: "1.2"
command: "PFDEBUG ENCODING"
syntax: "PFDEBUG ENCODING key"
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
PFDEBUG ENCODING key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the HyperLogLog's encoding: always `dense` in KiviDB, which does not use Redis's sparse encoding.

## Examples

```
> PFDEBUG ENCODING h
"dense"
```
