---
title: "FUNCTION KILL"
description: "Stops the function running, if it has not written."
version: "1.2"
command: "FUNCTION KILL"
syntax: "FUNCTION KILL"
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
FUNCTION KILL
```

**Available since:** 1.1.0
<!-- generated: end -->
Stops the function running, if it has not written. It is refused while a script started with `EVAL` is running: [`SCRIPT KILL`](script-kill.md) stops that.
