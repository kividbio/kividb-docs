---
title: "BACKUP ABORT"
description: "Cancels a backup that has not been sealed, while its snapshot is being written or while it is collecting writes."
version: "1.2"
command: "BACKUP ABORT"
syntax: "BACKUP ABORT"
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
BACKUP ABORT
```

**Available since:** 1.1.0
<!-- generated: end -->
Cancels a backup that has not been sealed, while its snapshot is being written or while it is collecting writes. It stops collecting at once; [`BACKUP STATUS`](backup-status.md) then gives the state `failed`, with the error `aborted`. Use it when a backup is no longer wanted, for example one started by mistake or one that is taking too long.

Its files are not deleted. [`BACKUP LIST`](backup-list.md) still lists the snapshot if it was complete, and the directory may hold the unfinished file of writes. [`BACKUP CLEANUP`](backup-cleanup.md) deletes them, and so does the next [`BACKUP START`](backup-start.md). A sealed backup cannot be aborted: delete it with `BACKUP CLEANUP`.

## Reply

- `OK`.
- `ERR no backup is in progress` when none was started, or it has failed or been aborted already.
- `ERR the backup is sealed; use BACKUP CLEANUP` for a sealed backup.

## Examples

```
> BACKUP START
OK
> BACKUP ABORT
OK
> BACKUP STATUS
1) "state"
2) "failed"
3) "error"
4) "aborted"
5) "start_time"
6) "1794254842"
7) "end_time"
8) "0"
> BACKUP LIST
1) "/tmp/k7700r/backupdir/appendonly.aof.3.base.kdb"
> BACKUP ABORT
(error) ERR no backup is in progress
> BACKUP CLEANUP
OK
```
