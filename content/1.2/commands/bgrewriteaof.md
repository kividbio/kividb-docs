---
title: "BGREWRITEAOF"
description: "Rewrites the append-only file in the background, as the shortest file that rebuilds the dataset."
version: "1.2"
command: "BGREWRITEAOF"
syntax: "BGREWRITEAOF"
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
BGREWRITEAOF
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Rewrites the append-only file in the background, as the shortest file that rebuilds the dataset.

The file is also rewritten on its own as it grows ([`auto-aof-rewrite-percentage`](../reference/configuration.md#auto-aof-rewrite-percentage)), whether it was on when the server started or turned on with `CONFIG SET appendonly yes`. Before 1.2, a file turned on with `CONFIG SET` was rewritten only by this command until the server restarted.

A rewrite saves a snapshot to `dump.kdb` as well, and moves [`LASTSAVE`](lastsave.md).

## Reply

- A status reply.
- `ERR AOF is not enabled`.
