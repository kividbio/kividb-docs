---
title: "FUNCTION LOAD"
description: "Load a function library (first line #!lua name=<library>)."
version: "1.2"
command: "FUNCTION LOAD"
syntax: "FUNCTION LOAD [REPLACE] library-code"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FUNCTION LOAD [REPLACE] library-code
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Load a function library (first line `#!lua name=<library>`). The code runs with only `redis.register_function`, `redis.log` and the version constants in reach — no `redis.call`, no `math` — and cannot set globals; it is stopped after 500 ms. A load is all of a library or none of it: an error leaves the library it was to replace as it was. A function's name belongs to one library. Library names are case-sensitive. Refused at the memory limit
