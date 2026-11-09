---
title: "FUNCTION HELP"
description: "Lists the FUNCTION subcommands, each with its arguments and a line on what it does, as the server knows them."
version: "1.2"
command: "FUNCTION HELP"
syntax: "FUNCTION HELP"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `FUNCTION` subcommands, each with its arguments and a line on what it does, as the server knows them. It is the quick reminder from inside a client; the [`FUNCTION`](function.md) page links to each subcommand's own page.

Functions are in the `lua` and `full` builds only: the default build answers `FUNCTION HELP`, like every `FUNCTION` subcommand, with `ERR this build of KiviDB has no Lua: ...`. See [Scripting](../guides/scripting.md#functions).

## Reply

An array of strings: a heading, then, for each subcommand, its syntax and an indented description.

## Examples

```
> FUNCTION HELP
 1) FUNCTION <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) LOAD [REPLACE] <FUNCTION CODE>
 3)     Create a new library with the given library name and code.
 4) DELETE <LIBRARY NAME>
 5)     Delete the given library.
 6) LIST [LIBRARYNAME <pattern>] [WITHCODE]
 7)     Return general information on all the libraries.
...
16) RESTORE <PAYLOAD> [FLUSH|APPEND|REPLACE]
17)     Restore the libraries represented by the given payload.
18) HELP
19)     Print this help.
```

A subcommand that does not exist gets an error, which, unlike Redis's, does not point to `FUNCTION HELP`:

```
> FUNCTION NOPE
(error) ERR unknown subcommand 'NOPE'
```
