---
title: "BACKUP SEAL"
description: "Ends the backup: it now holds everything up to this moment, and its manifest is written."
version: "1.1"
command: "BACKUP SEAL"
syntax: "BACKUP SEAL"
group: "other"
since: "1.1.0"
history: []
container: "BACKUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BACKUP SEAL
```

**Available since:** 1.1.0
<!-- generated: end -->
Ends the backup: it now holds everything up to this moment, and its manifest is written.

## Reply

- `OK`.
- `ERR the base snapshot is still being written; try again`.

## Examples

```
> BACKUP SEAL
OK
> BACKUP STATUS
1) "state"
2) "sealed"
...
```
