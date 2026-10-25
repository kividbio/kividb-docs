---
title: "CLIENT GETNAME"
description: "Returns the connection's name, or nil."
version: "1.2"
command: "CLIENT GETNAME"
syntax: "CLIENT GETNAME"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT GETNAME
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the connection's name, or `nil`.

## Examples

```
> CLIENT GETNAME
"worker-1"
```
