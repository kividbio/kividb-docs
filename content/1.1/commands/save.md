---
title: "SAVE"
description: "Writes a snapshot of the dataset to dump.kdb, in the working directory, before replying."
version: "1.1"
command: "SAVE"
syntax: "SAVE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SAVE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Writes a snapshot of the dataset to `dump.kdb`, in the working directory, before replying. Clients wait meanwhile; [`BGSAVE`](bgsave.md) does not make them.

## Examples

```
> SAVE
OK
```
