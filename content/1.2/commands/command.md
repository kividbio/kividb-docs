---
title: "COMMAND"
description: "Returns every command, each as an array: its name, its arity (a negative number is a minimum), its flags, the positions of its first and last key and the step between them, and its ACL categories."
version: "1.2"
command: "COMMAND"
syntax: "COMMAND"
group: "server"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["server", "slow"]
history: []
subcommands: ["COMMAND COUNT", "COMMAND DOCS", "COMMAND GETKEYS", "COMMAND GETKEYSANDFLAGS", "COMMAND HELP", "COMMAND INFO", "COMMAND LIST"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
COMMAND
```

**Available since:** 1.1.0 · **ACL categories:** `@server`, `@slow`

Subcommands: [COMMAND COUNT](command-count.md), [COMMAND DOCS](command-docs.md), [COMMAND GETKEYS](command-getkeys.md), [COMMAND GETKEYSANDFLAGS](command-getkeysandflags.md), [COMMAND HELP](command-help.md), [COMMAND INFO](command-info.md), [COMMAND LIST](command-list.md)
<!-- generated: end -->
Returns every command, each as an array: its name, its arity (a negative number is a minimum), its flags, the positions of its first and last key and the step between them, and its ACL categories. A command whose keys depend on its arguments has the `movablekeys` flag. Cluster clients route by this.

## Examples

```
> COMMAND INFO GET
1) 1) "get"
   2) (integer) 2
   3) 1) readonly
      2) fast
   4) (integer) 1
   5) (integer) 1
   6) (integer) 1
   7) 1) "@fast"
      2) "@read"
      3) "@string"
   ...
```
