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
Returns the paths of the backup's files that are complete and safe to copy: the snapshot; once sealed, also the writes and the manifest.

## Examples

```
> BACKUP LIST
1) "/data/backupdir/appendonly.aof.1.base.kdb"
2) "/data/backupdir/appendonly.aof.1.incr.aof"
3) "/data/backupdir/appendonly.aof.manifest"
```
