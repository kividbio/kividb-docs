---
title: "BACKUP CLEANUP"
description: "Removes the files of a sealed or failed backup."
version: "1.2"
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

A backup in the directory when the server starts is found again: a sealed one stays sealed, and one the restart cut short is failed; this command deletes either. Before 1.2, after a restart it replied `ERR there is no backup to clean up`, and the files had to be deleted by hand.

## Reply

- `OK`.
- `ERR a backup is in progress; seal or abort it first`.
- `ERR there is no backup to clean up`.
