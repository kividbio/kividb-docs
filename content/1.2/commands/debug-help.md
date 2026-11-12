---
title: "DEBUG HELP"
description: "Lists the DEBUG subcommands, with a line on what each does, as Redis does."
version: "1.2"
command: "DEBUG HELP"
syntax: "DEBUG HELP"
group: "server"
since: "1.2.1"
history: []
container: "DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG HELP
```

**Available since:** 1.2.1
<!-- generated: end -->
Lists the [`DEBUG`](debug.md) subcommands, with a line on what each does, as Redis does. Since 1.2.1; before, `DEBUG HELP` replied `OK`.

## Reply

An array of simple strings: a line for each subcommand and its arguments, each followed by a line that describes it, indented.

## Examples

```
> DEBUG HELP
 1) DEBUG <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) DIGEST-VALUE <key> [<key> ...]
 3)     A digest of each key's value, or 40 zeros for a key that is not there.
 4) LOG <message>
 5)     Write <message> to the server log.
...
20) SLEEP <seconds>
21)     Block this connection's worker thread for <seconds>.
22) HELP
23)     Print this help.
```
