---
title: "CONFIG GET"
description: "Returns the settings whose names match a glob-style pattern, * for all, as name-value pairs."
version: "1.2"
command: "CONFIG GET"
syntax: "CONFIG GET parameter [parameter ...]"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG GET parameter [parameter ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the settings whose names match a glob-style pattern, `*` for all, as name-value pairs.

## Examples

```
> CONFIG GET maxmemory*
1) "maxmemory"
2) "0"
3) "maxmemory-policy"
4) "noeviction"
5) "maxmemory-samples"
6) "5"
7) "maxmemory-clients"
8) "0"
```
