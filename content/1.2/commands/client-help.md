---
title: "CLIENT HELP"
description: "Lists the CLIENT subcommands, one line each with its arguments, followed by an indented line saying what it does."
version: "1.2"
command: "CLIENT HELP"
syntax: "CLIENT HELP"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`CLIENT`](client.md) subcommands, one line each with its arguments, followed by an indented line saying what it does. It is the server's own summary, useful from a command line; this reference has a page for each subcommand.

## Reply

An array of status lines.

## Examples

```
> CLIENT HELP
 1) CLIENT <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) CACHING (YES|NO)
 3)     Enable/disable tracking of the keys for next command in OPTIN/OPTOUT modes.
 4) GETREDIR
 5)     Return the client ID we are redirecting to when tracking is enabled.
...
38) HELP
39)     Print this help.
```
