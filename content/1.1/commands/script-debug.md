---
title: "SCRIPT DEBUG"
description: "Accepted for compatibility with Redis, with YES, SYNC or NO."
version: "1.1"
command: "SCRIPT DEBUG"
syntax: "SCRIPT DEBUG YES | SYNC | NO"
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
SCRIPT DEBUG YES | SYNC | NO
```

**Available since:** 1.1.0
<!-- generated: end -->
Accepted for compatibility with Redis, with `YES`, `SYNC` or `NO`. There is no Lua debugger: scripts run as usual.
