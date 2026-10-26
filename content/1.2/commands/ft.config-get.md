---
title: "FT.CONFIG GET"
description: "Returns settings matching a name or pattern, * for all, as [name, value] pairs."
version: "1.2"
command: "FT.CONFIG GET"
syntax: "FT.CONFIG GET option|pattern"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG GET option|pattern
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns settings matching a name or pattern, `*` for all, as `[name, value]` pairs.

## Examples

```
> FT.CONFIG GET TIMEOUT
1) 1) "TIMEOUT"
   2) "500"
```
