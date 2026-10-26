---
title: "CLIENT GETREDIR"
description: "Returns the connection this one sends its invalidations to; -1 if tracking is off or it does not redirect."
version: "1.1"
command: "CLIENT GETREDIR"
syntax: "CLIENT GETREDIR"
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
CLIENT GETREDIR
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the connection this one sends its invalidations to; `-1` if tracking is off or it does not redirect.

## Examples

```
> CLIENT GETREDIR
(integer) -1
```
