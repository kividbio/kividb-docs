---
title: "COMMAND"
description: "Every command, each as [name, arity, [flags], first-key, last-key, key-step, [@categories], [], [], []]."
version: "1.1"
command: "COMMAND"
syntax: "COMMAND"
group: "server"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["server", "slow"]
history: []
subcommands: ["COMMAND COUNT", "COMMAND DOCS", "COMMAND GETKEYS", "COMMAND GETKEYSANDFLAGS", "COMMAND INFO", "COMMAND LIST"]
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
COMMAND
```

**Available since:** 1.1.0 · **ACL categories:** `@server`, `@slow`

Subcommands: [COMMAND COUNT](command-count.md), [COMMAND DOCS](command-docs.md), [COMMAND GETKEYS](command-getkeys.md), [COMMAND GETKEYSANDFLAGS](command-getkeysandflags.md), [COMMAND INFO](command-info.md), [COMMAND LIST](command-list.md)
<!-- generated: end -->
## Description

Every command, each as `[name, arity, [flags], first-key, last-key, key-step, [@categories], [], [], []]`. The three key numbers say where a command's keys are (a negative `last-key` counts from the end); a command whose keys depend on its arguments has the `movablekeys` flag, and `COMMAND GETKEYS` answers for it. This is what redis-py's cluster client routes by. The arity is a lower bound
