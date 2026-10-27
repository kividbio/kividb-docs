---
title: "BGSAVE"
description: "Writes a snapshot of the dataset to dump.kdb in the background, and replies at once."
version: "1.2"
command: "BGSAVE"
syntax: "BGSAVE"
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BGSAVE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Writes a snapshot of the dataset to `dump.kdb` in the background, and replies at once.

The snapshot is the dataset at one moment: a transaction, a script or an `MSET` is in it whole or not at all. Before 1.2, with the append-only file off, the dataset was copied a part at a time, and a transaction whose keys were in two parts could be saved half applied.

## Examples

```
> BGSAVE
Background saving started
```
