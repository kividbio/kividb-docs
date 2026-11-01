---
title: "PFDEBUG ENCODING"
description: "Returns the HyperLogLog's encoding: dense, or sparse for one Redis wrote that has not been written to since."
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
Returns the HyperLogLog's encoding: `dense`, or `sparse` for one Redis wrote that has not been written to since. KiviDB writes only dense ones.

## Examples

```
> PFDEBUG ENCODING h
"dense"
```
