---
title: "OBJECT HELP"
description: "Lists the OBJECT subcommands, each with a line or two on what it does."
version: "1.2"
command: "OBJECT HELP"
syntax: "OBJECT HELP"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
OBJECT HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the [`OBJECT`](object.md) subcommands, each with a line or two on what it does. It takes no arguments.

The text is the same as Redis's. KiviDB keeps one representation per type, so [`OBJECT ENCODING`](object-encoding.md) answers with the name Redis would use, and [`OBJECT REFCOUNT`](object-refcount.md) is always `1`; [`OBJECT IDLETIME`](object-idletime.md) and [`OBJECT FREQ`](object-freq.md) are kept only under the matching `maxmemory-policy`.

## Reply

An array of strings.

## Examples

```
> OBJECT HELP
 1) OBJECT <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) ENCODING <key>
 3)     Return the kind of internal representation used in order to store the value
 4)     associated with a <key>.
 5) FREQ <key>
...
14) HELP
15)     Print this help.
> OBJECT HELP extra
(error) ERR wrong number of arguments for 'object|help' command
```
