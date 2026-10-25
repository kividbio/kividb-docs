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

## Examples

```
> BGSAVE
Background saving started
```
