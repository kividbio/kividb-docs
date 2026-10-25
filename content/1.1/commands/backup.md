---
title: "BACKUP"
description: "Takes a consistent backup of the dataset while the server keeps serving: a snapshot as of the start, then the writes that follow, up to the moment it is sealed."
version: "1.1"
command: "BACKUP"
syntax: "BACKUP"
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["BACKUP ABORT", "BACKUP CLEANUP", "BACKUP HELP", "BACKUP LIST", "BACKUP SEAL", "BACKUP START", "BACKUP STATUS"]
# generated: end
status: "reviewed"
group_override: "server"
---

<!-- generated: start -->
## Syntax

```
BACKUP
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [BACKUP ABORT](backup-abort.md), [BACKUP CLEANUP](backup-cleanup.md), [BACKUP HELP](backup-help.md), [BACKUP LIST](backup-list.md), [BACKUP SEAL](backup-seal.md), [BACKUP START](backup-start.md), [BACKUP STATUS](backup-status.md)
<!-- generated: end -->
Takes a consistent backup of the dataset while the server keeps serving: a snapshot as of the start, then the writes that follow, up to the moment it is sealed. KiviDB's own command. See its subcommands.

A sealed backup is three files in the backup directory, `backupdir` under the working directory unless `backupdirname` says otherwise: `appendonly.aof.N.base.kdb`, `appendonly.aof.N.incr.aof` and `appendonly.aof.manifest`. Restoring it gives the dataset as it was when it was sealed, not when it started, so the nodes of a cluster can each start a backup in turn and then be sealed together. It works with the AOF on or off, on a master or a replica.

To start a server from a backup:

```bash
kividb --preload-file aof:/path/to/appendonly.aof.manifest   # a sealed backup
kividb --preload-file rdb:/path/to/dump.kdb                  # a single snapshot
```

The file given is loaded instead of the usual `dump.kdb` and `appendonly.aof`; one that cannot be loaded stops the server. `backup-sealed-ttl` removes a sealed backup after that many seconds; `0`, the default, keeps it.
