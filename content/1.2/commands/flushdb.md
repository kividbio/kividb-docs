---
title: "FLUSHDB"
description: "Deletes every key of the current database."
version: "1.2"
command: "FLUSHDB"
syntax: "FLUSHDB"
group: "server"
since: "1.1.0"
arity: -1
flags: ["write"]
acl_categories: ["dangerous", "server", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FLUSHDB
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Deletes every key of the current database. `ASYNC` frees them in the background, `SYNC` at once.

## Examples

```
> FLUSHDB ASYNC
OK
```
