---
title: "COMMAND GETKEYS"
description: "Returns the keys a command would use, given its arguments."
version: "1.2"
command: "COMMAND GETKEYS"
syntax: "COMMAND GETKEYS command [arg ...]"
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
COMMAND GETKEYS command [arg ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the keys a command would use, given its arguments.

## Examples

```
> COMMAND GETKEYS MSET a 1 b 2
1) "a"
2) "b"
```
