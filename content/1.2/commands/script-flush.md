---
title: "SCRIPT FLUSH"
description: "Empties the script cache."
version: "1.2"
command: "SCRIPT FLUSH"
syntax: "SCRIPT FLUSH [ASYNC | SYNC]"
group: "scripting"
since: "1.1.0"
history: []
container: "SCRIPT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCRIPT FLUSH [ASYNC | SYNC]
```

**Available since:** 1.1.0
<!-- generated: end -->
Empties the script cache. `ASYNC` and `SYNC` are accepted.

## Examples

```
> SCRIPT FLUSH
OK
```
