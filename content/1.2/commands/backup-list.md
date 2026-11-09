---
title: "BACKUP LIST"
description: "Returns the paths of the backup's files that are complete and safe to copy: the snapshot; once sealed, also the writes and the manifest."
version: "1.2"
command: "BACKUP LIST"
syntax: "BACKUP LIST"
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
BACKUP LIST
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the full paths of the backup's files that are complete and safe to copy. Use it to know what to copy away, and when: a file that is listed will not change again.

What it lists depends on the backup's state ([`BACKUP STATUS`](backup-status.md)):

- `snapshotting`: nothing yet; the snapshot is still being written.
- `incrementing`: the snapshot, `appendonly.aof.N.base.kdb`. It can be copied while the writes that follow are still being collected.
- `sealed`: the snapshot, the writes, `appendonly.aof.N.incr.aof`, and the manifest, `appendonly.aof.manifest`. Copy all three; the manifest is what a server restores from.
- `failed`: what was complete when it failed or was aborted, such as the snapshot. Those files are not a backup to restore from.
- `idle`: nothing.

`N` is the backup's number, which goes up with each backup. The files are in [`backupdirname`](../reference/configuration.md#backupdirname), under the working directory. A sealed backup is listed again after a restart, until [`BACKUP CLEANUP`](backup-cleanup.md) or [`backup-sealed-ttl`](../reference/configuration.md#backup-sealed-ttl) deletes it.

## Reply

An array of paths; an empty array when there is nothing to copy.

## Examples

```
> BACKUP START
OK
> BACKUP LIST
(empty array)
> BACKUP LIST
1) "/tmp/k7700r/backupdir/appendonly.aof.2.base.kdb"
> BACKUP SEAL
OK
> BACKUP LIST
1) "/tmp/k7700r/backupdir/appendonly.aof.2.base.kdb"
2) "/tmp/k7700r/backupdir/appendonly.aof.2.incr.aof"
3) "/tmp/k7700r/backupdir/appendonly.aof.manifest"
```
