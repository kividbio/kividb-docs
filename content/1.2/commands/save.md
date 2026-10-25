---
title: "SAVE"
description: "Writes a snapshot of the dataset to dump.kdb, in the working directory, before replying."
version: "1.2"
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

## Known issue

With the append-only file off, the dataset is copied a part at a time rather than at one moment: a transaction or script whose keys are in two parts can be saved half applied. Filed as [kividb#148](https://github.com/kividbio/kividb/issues/148).

## Examples

```
> SAVE
OK
```
