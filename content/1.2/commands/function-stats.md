---
title: "FUNCTION STATS"
description: "Returns the function running, if any (its name, command and duration so far), and the number of libraries and functions."
version: "1.2"
command: "FUNCTION STATS"
syntax: "FUNCTION STATS"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION STATS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the function running, if any (its name, command and duration so far), and the number of libraries and functions.

## Examples

```
> FUNCTION STATS
1) "running_script"
2) (nil)
3) "engines"
4) 1) "LUA"
   2) 1) "libraries_count"
      2) (integer) 1
      3) "functions_count"
      4) (integer) 2
```
