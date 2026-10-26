---
title: "HIMPORT"
description: "Loads many hashes that have the same fields, without sending the field names for each: a command of Redis 8.10."
version: "1.1"
command: "HIMPORT"
syntax: "HIMPORT"
group: "hash"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "write"]
acl_categories: ["hash", "slow", "write"]
history: []
subcommands: ["HIMPORT DISCARD", "HIMPORT PREPARE", "HIMPORT SET"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HIMPORT
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`

Subcommands: [HIMPORT DISCARD](himport-discard.md), [HIMPORT PREPARE](himport-prepare.md), [HIMPORT SET](himport-set.md)
<!-- generated: end -->
Loads many hashes that have the same fields, without sending the field names for each: a command of Redis 8.10. A client first names a list of fields, a fieldset, with [`HIMPORT PREPARE`](himport-prepare.md), then creates hashes from it with [`HIMPORT SET`](himport-set.md), giving only the values.

Fieldsets belong to the connection that made them, and go when it closes.
