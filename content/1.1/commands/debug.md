---
title: "DEBUG"
description: "Accepted for compatibility with Redis tools."
version: "1.1"
command: "DEBUG"
syntax: "DEBUG ..."
group: "server"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG ...
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Accepted for compatibility with Redis tools. `DEBUG SLEEP seconds` makes the server sleep that long, which is useful for testing timeouts; every other subcommand replies `OK` and does nothing.
