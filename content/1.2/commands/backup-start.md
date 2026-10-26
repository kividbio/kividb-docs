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

## Known issue

After a restart, a sealed backup's files are left in the directory, and it refuses to start until they are deleted by hand. Filed as [kividb#150](https://github.com/kividbio/kividb/issues/150).

## Reply

- `OK`.
- `ERR a backup is already in progress`.

## Examples

```
> BACKUP START
OK
> BACKUP STATUS
1) "state"
2) "snapshotting"
...
```
