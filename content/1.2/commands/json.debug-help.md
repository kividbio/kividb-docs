---
title: "JSON.DEBUG HELP"
description: "Lists the JSON.DEBUG subcommands and what each does."
version: "1.2"
command: "JSON.DEBUG HELP"
syntax: "JSON.DEBUG HELP"
group: "json"
since: "1.1.0"
history: []
container: "JSON.DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.DEBUG HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`JSON.DEBUG`](json.debug.md) subcommands, one line each, with their arguments and what they do. The subcommand name is not case-sensitive, so `JSON.DEBUG help` works too. Any other subcommand, or none, fails with an error that points here.

## Reply

An array of strings, one per subcommand.

## Examples

```
> JSON.DEBUG HELP
1) "MEMORY <key> [path] - reports memory usage"
2) "HELP                - this message"
> JSON.DEBUG FOO
(error) ERR unknown subcommand - try `JSON.DEBUG HELP`
```
