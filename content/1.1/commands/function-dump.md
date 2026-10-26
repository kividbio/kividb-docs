---
title: "FUNCTION DUMP"
description: "Serializes every function library into a payload that FUNCTION RESTORE loads, on this server or another."
version: "1.1"
command: "FUNCTION DUMP"
syntax: "FUNCTION DUMP"
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
FUNCTION DUMP
```

**Available since:** 1.1.0
<!-- generated: end -->
Serializes every function library into a payload that [`FUNCTION RESTORE`](function-restore.md) loads, on this server or another. The format is KiviDB's own. Only the `lua` and `full` builds have functions.
