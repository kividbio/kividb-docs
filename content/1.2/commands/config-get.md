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
Returns the settings whose names match a glob-style pattern, `*` for all, as name-value pairs. Several patterns can be given at once, and a setting that matches more than one is returned once. A pattern that matches nothing gives an empty array, not an error.

Values are given as `CONFIG SET` would take them, sizes in bytes. [Configuration](../reference/configuration.md) lists every setting, its default, and whether it can be changed at run time.

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
> CONFIG GET port bind
1) "bind"
2) "0.0.0.0"
3) "port"
4) "6380"
> CONFIG GET nope
(empty array)
```
