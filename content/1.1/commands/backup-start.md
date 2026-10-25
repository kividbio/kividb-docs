---
title: "BACKUP START"
description: "Starts a backup: writes a snapshot of the dataset as of now into the backup directory, then collects the writes that follow."
version: "1.1"
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
