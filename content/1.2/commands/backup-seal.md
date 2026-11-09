---
title: "BACKUP SEAL"
description: "Ends the backup: it now holds everything up to this moment, and its manifest is written."
version: "1.2"
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
Ends the backup [`BACKUP START`](backup-start.md) began: it stops collecting writes, flushes them to disk as `appendonly.aof.N.incr.aof`, and writes the manifest, `appendonly.aof.manifest`. The backup now holds the dataset as it is at this moment: restored, it has every write made before the seal and none made after. Use it once you want the backup to end; on a cluster, start a backup on each node in turn, then seal them together.

The snapshot must be written first: while [`BACKUP STATUS`](backup-status.md) says `snapshotting`, the seal is refused; wait for `incrementing` and try again. Once sealed, the state is `sealed` with an `end_time`, [`BACKUP LIST`](backup-list.md) lists the three files, and no other backup can start until [`BACKUP CLEANUP`](backup-cleanup.md), or [`backup-sealed-ttl`](../reference/configuration.md#backup-sealed-ttl) seconds after the seal, deletes it. To restore it, start a server with `--preload-file aof:<path to the manifest>` ([Persistence](../guides/persistence.md#backups)).

## Reply

- `OK`.
- `ERR the base snapshot is still being written; try again` while the state is `snapshotting`.
- `ERR no backup is in progress` when there is none to seal: none was started, or it is sealed, failed or aborted already.
- `ERR the backup is already being sealed` if another connection is sealing it.
- `ERR could not seal the backup: ...` if the files cannot be written; the backup is then `failed`.

## Examples

```
> BACKUP START
OK
> BACKUP SEAL
(error) ERR the base snapshot is still being written; try again
> BACKUP STATUS
1) "state"
2) "incrementing"
...
> SET afterstart yes
OK
> BACKUP SEAL
OK
> BACKUP STATUS
1) "state"
2) "sealed"
3) "error"
4) ""
5) "start_time"
6) "1794254839"
7) "end_time"
8) "1794254842"
> BACKUP SEAL
(error) ERR no backup is in progress
```
