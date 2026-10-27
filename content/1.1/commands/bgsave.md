---
title: "BGSAVE"
description: "Writes a snapshot of the dataset to dump.kdb in the background, and replies at once."
version: "1.1"
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

## Known issue

With the append-only file off, the dataset is copied a part at a time rather than at one moment: a transaction or script whose keys are in two parts can be saved half applied. Filed as [kividb#148](https://github.com/kividbio/kividb/issues/148), fixed in 1.2.

## Examples

```
> BGSAVE
Background saving started
```
