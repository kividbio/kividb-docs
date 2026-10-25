---
title: "FUNCTION LIST"
description: "Returns every library, or those whose names match LIBRARYNAME pattern, with its functions, each with its description and flags."
version: "1.1"
command: "FUNCTION LIST"
syntax: "FUNCTION LIST [LIBRARYNAME pattern] [WITHCODE]"
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
FUNCTION LIST [LIBRARYNAME pattern] [WITHCODE]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns every library, or those whose names match `LIBRARYNAME pattern`, with its functions, each with its description and flags. `WITHCODE` adds the library's code.

## Examples

```
> FUNCTION LIST
1) 1) "library_name"
   2) "mylib"
   3) "engine"
   4) "LUA"
   5) "functions"
   6) 1) 1) "name"
         2) "hello"
         3) "description"
         4) (nil)
         5) "flags"
         6) (empty array)
      2) 1) "name"
         2) "getk"
         3) "description"
         4) "read a key"
         5) "flags"
         6) 1) "no-writes"
```
