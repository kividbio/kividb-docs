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

## Reply

- A status reply.
- `ERR AOF is not enabled`.
