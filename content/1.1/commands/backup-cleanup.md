---
title: "BACKUP CLEANUP"
description: "Removes the files of a sealed or failed backup."
version: "1.1"
command: "BACKUP CLEANUP"
syntax: "BACKUP CLEANUP"
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
BACKUP CLEANUP
```

**Available since:** 1.1.0
<!-- generated: end -->
Removes the files of a sealed or failed backup.

## Reply

- `OK`.
- `ERR a backup is in progress; seal or abort it first`.
- `ERR there is no backup to clean up`.
