---
title: "CONFIG HELP"
description: "Lists the CONFIG subcommands and what each does."
version: "1.2"
command: "CONFIG HELP"
syntax: "CONFIG HELP"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `CONFIG` subcommands, one line each with its arguments, followed by an indented line saying what it does: [`CONFIG GET`](config-get.md), [`CONFIG SET`](config-set.md), [`CONFIG RESETSTAT`](config-resetstat.md), [`CONFIG REWRITE`](config-rewrite.md) and `CONFIG HELP`. The text is the server's own summary; each subcommand has its own page here.

## Reply

An array of status lines.

## Examples

```
> CONFIG HELP
 1) CONFIG <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) GET <pattern>
 3)     Return parameters matching the glob-like <pattern> and their values.
 4) SET <directive> <value>
 5)     Set the configuration <directive> to <value>.
...
```
