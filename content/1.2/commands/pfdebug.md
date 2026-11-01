---
title: "PFDEBUG"
description: "Inspects or converts a HyperLogLog."
version: "1.2"
command: "PFDEBUG"
syntax: "PFDEBUG"
group: "hyperloglog"
since: "1.1.0"
arity: 3
flags: ["admin", "write"]
acl_categories: ["admin", "dangerous", "hyperloglog", "slow", "write"]
history: [{"release": "1.2.0", "change": "flags: added write; removed readonly; acl categories: added write; removed read"}]
subcommands: ["PFDEBUG DECODE", "PFDEBUG ENCODING", "PFDEBUG GETREG", "PFDEBUG RESET", "PFDEBUG TODENSE"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFDEBUG
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@hyperloglog`, `@slow`, `@write`

Subcommands: [PFDEBUG DECODE](pfdebug-decode.md), [PFDEBUG ENCODING](pfdebug-encoding.md), [PFDEBUG GETREG](pfdebug-getreg.md), [PFDEBUG RESET](pfdebug-reset.md), [PFDEBUG TODENSE](pfdebug-todense.md)

**History:**

- 1.2.0: flags: added write; removed readonly; acl categories: added write; removed read
<!-- generated: end -->
Inspects or converts a HyperLogLog. See its subcommands.

Since 1.2 it is flagged as a write, since `TODENSE` and `RESET` change the value; they reach replicas and the append-only file like any write. `GETREG` only reads, unlike Redis's, where it converts a sparse value to dense first.
