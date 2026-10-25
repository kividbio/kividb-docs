---
title: "FUNCTION RESTORE"
description: "Loads a payload from FUNCTION DUMP."
version: "1.1"
command: "FUNCTION RESTORE"
syntax: "FUNCTION RESTORE"
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
FUNCTION RESTORE
```

**Available since:** 1.1.0
<!-- generated: end -->
Loads a payload from [`FUNCTION DUMP`](function-dump.md).

| Policy | Effect |
|---|---|
| `APPEND` | Add the payload's libraries; fail if one exists already (the default). |
| `REPLACE` | Add them, replacing libraries of the same name. |
| `FLUSH` | Delete every library first. |

## Reply

- `OK`.
- `ERR Library mylib already exists`, under `APPEND`.
