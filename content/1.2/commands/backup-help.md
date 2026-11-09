---
title: "BACKUP HELP"
description: "Lists the BACKUP subcommands and a line on what each does: START, LIST, SEAL, CLEANUP, ABORT, STATUS and HELP itself."
version: "1.2"
command: "BACKUP HELP"
syntax: "BACKUP HELP"
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
BACKUP HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `BACKUP` subcommands and a line on what each does: [`START`](backup-start.md), [`LIST`](backup-list.md), [`SEAL`](backup-seal.md), [`CLEANUP`](backup-cleanup.md), [`ABORT`](backup-abort.md), [`STATUS`](backup-status.md) and `HELP` itself. It changes nothing, and works in any state of a backup. None of the subcommands takes an argument. [`BACKUP`](backup.md) and [Persistence](../guides/persistence.md#backups) explain how a backup is taken and restored.

## Reply

An array of lines of text.

## Examples

```
> BACKUP HELP
 1) BACKUP <subcommand>. Subcommands are:
 2) START
 3)     Open a backup: write a base snapshot and start collecting writes.
 4) LIST
 5)     Return the paths of the backup files that are complete.
 6) SEAL
 7)     Freeze the backup at this moment and write its manifest.
...
14) HELP
15)     Print this help.
```
