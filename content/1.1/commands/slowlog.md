---
title: "SLOWLOG"
description: "SLOWLOG and its subcommands."
version: "1.1"
command: "SLOWLOG"
syntax: "SLOWLOG"
group: "observability"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["SLOWLOG GET", "SLOWLOG LEN", "SLOWLOG RESET"]
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SLOWLOG
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [SLOWLOG GET](slowlog-get.md), [SLOWLOG LEN](slowlog-len.md), [SLOWLOG RESET](slowlog-reset.md)
<!-- generated: end -->
