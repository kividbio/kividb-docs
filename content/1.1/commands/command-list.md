---
title: "COMMAND LIST"
description: "Returns the names of every command, or of those matching a FILTERBY: PATTERN pattern, ACLCAT category, or MODULE module (always empty)."
version: "1.1"
command: "COMMAND LIST"
syntax: "COMMAND LIST [FILTERBY MODULE module | ACLCAT category | PATTERN pattern]"
group: "server"
since: "1.1.0"
history: []
container: "COMMAND"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
COMMAND LIST [FILTERBY MODULE module | ACLCAT category | PATTERN pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the names of every command, or of those matching a `FILTERBY`: `PATTERN pattern`, `ACLCAT category`, or `MODULE module` (always empty).

## Examples

```
> COMMAND LIST FILTERBY PATTERN xa*
1) "xack"
2) "xadd"
3) "xautoclaim"
4) "xackdel"
```
