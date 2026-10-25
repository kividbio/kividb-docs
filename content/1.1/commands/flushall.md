---
title: "FLUSHALL"
description: "Deletes every key of every database."
version: "1.1"
command: "FLUSHALL"
syntax: "FLUSHALL"
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
FLUSHALL
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Deletes every key of every database. `ASYNC` frees them in the background, `SYNC` at once.

## Examples

```
> FLUSHALL SYNC
OK
```
