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
Returns the value of each search setting whose name matches `pattern`: an exact name such as `TIMEOUT`, or a glob-style pattern, `*` for every setting. Names are matched without regard to case. Use it to check what a setting is before changing it with [`FT.CONFIG SET`](ft.config-set.md); [`FT.CONFIG`](ft.config.md) says which settings are acted on.

A name that matches nothing returns an empty array, not an error. Settings are listed in a fixed order, not sorted.

## Reply

An array with a `[name, value]` pair for each setting that matches, values as strings; a map over RESP3.

## Examples

```
> FT.CONFIG GET TIMEOUT
1) 1) "TIMEOUT"
   2) "0"
> FT.CONFIG GET *timeout
1) 1) "TIMEOUT"
   2) "0"
2) 1) "ON_TIMEOUT"
   2) "return"
> FT.CONFIG GET *
 1) 1) "CURSOR_MAX_IDLE"
    2) "300000"
 2) 1) "TIMEOUT"
    2) "0"
...
23) 1) "BM25STD_TANH_FACTOR"
    2) "4"
> FT.CONFIG GET NOPE
(empty array)
> FT.CONFIG GET
(error) ERR wrong number of arguments for 'FT.CONFIG|GET' command
```
