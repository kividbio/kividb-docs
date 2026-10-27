---
title: "BACKUP START"
description: "Starts a backup: writes a snapshot of the dataset as of now into the backup directory, then collects the writes that follow."
version: "1.2"
command: "BACKUP START"
syntax: "BACKUP START"
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
BACKUP START
```

**Available since:** 1.1.0
<!-- generated: end -->
Starts a backup: writes a snapshot of the dataset as of now into the backup directory, then collects the writes that follow.

A sealed backup must be deleted with [`BACKUP CLEANUP`](backup-cleanup.md), or by [`backup-sealed-ttl`](../reference/configuration.md#backup-sealed-ttl), before another starts. A failed one, such as one a restart cut short, is deleted by this command. Both are found again after a restart; before 1.2, their files stayed in the directory, and this command refused to start until they were deleted by hand.

## Reply

- `OK`.
- `ERR a backup is already in progress`.
- `ERR a sealed backup is waiting for BACKUP CLEANUP before another can start`.

## Examples

```
> BACKUP START
OK
> BACKUP STATUS
1) "state"
2) "snapshotting"
...
```
