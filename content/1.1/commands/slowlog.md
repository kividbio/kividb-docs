---
title: "SLOWLOG"
description: "The slow log: the commands that took longer than slowlog-log-slower-than microseconds to run, up to slowlog-max-len entries (128 by default)."
version: "1.1"
command: "SLOWLOG"
syntax: "SLOWLOG"
group: "observability"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["SLOWLOG GET", "SLOWLOG HELP", "SLOWLOG LEN", "SLOWLOG RESET"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SLOWLOG
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [SLOWLOG GET](slowlog-get.md), [SLOWLOG HELP](slowlog-help.md), [SLOWLOG LEN](slowlog-len.md), [SLOWLOG RESET](slowlog-reset.md)
<!-- generated: end -->
The slow log: the commands that took longer than `slowlog-log-slower-than` microseconds to run, up to `slowlog-max-len` entries (128 by default). `slowlog-log-slower-than` is `-1` by default, which logs nothing: unlike Redis, whose default is 10,000, KiviDB's slow log is off until it is set. `0` logs every command. The time is how long the command ran, not the time spent waiting or reading it. See its subcommands.
