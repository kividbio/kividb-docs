---
title: "JSON.DEBUG"
description: "A container for commands that report on JSON documents rather than read or change them."
version: "1.2"
command: "JSON.DEBUG"
syntax: "JSON.DEBUG"
group: "json"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: []
subcommands: ["JSON.DEBUG HELP", "JSON.DEBUG MEMORY"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.DEBUG
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`

Subcommands: [JSON.DEBUG HELP](json.debug-help.md), [JSON.DEBUG MEMORY](json.debug-memory.md)
<!-- generated: end -->
A container for commands that report on JSON documents rather than read or change them. On its own, or with a subcommand it does not know, it replies with an error that points to [`JSON.DEBUG HELP`](json.debug-help.md).

| Subcommand | What it does |
|---|---|
| [`JSON.DEBUG MEMORY`](json.debug-memory.md) | The size, in bytes, of each value a path matches, as compact JSON text. |
| [`JSON.DEBUG HELP`](json.debug-help.md) | Lists the subcommands. |

The subcommand name is not case-sensitive.

## Examples

```
> JSON.SET d $ '{"name":"Ada"}'
OK
> JSON.DEBUG MEMORY d
(integer) 14
> JSON.DEBUG
(error) ERR unknown subcommand - try `JSON.DEBUG HELP`
```
