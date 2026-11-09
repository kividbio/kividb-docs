---
title: "COMMAND LIST"
description: "Returns the names of every command, or of those matching a FILTERBY:"
version: "1.2"
command: "COMMAND LIST"
syntax: "COMMAND LIST [FILTERBY MODULE module | ACLCAT category | PATTERN pattern]"
group: "server"
since: "1.1.0"
history: []
container: "COMMAND"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
COMMAND LIST [FILTERBY MODULE module | ACLCAT category | PATTERN pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the names of every command, or of those matching a `FILTERBY`:

- `PATTERN pattern`: names matching a glob-style pattern. Subcommands are listed as `container|subcommand`, so `client*` gives `client` and each `client|...`.
- `ACLCAT category`: the commands in an [ACL category](acl-cat.md), such as `hyperloglog`.
- `MODULE module`: the commands of a built-in module, by the name [`MODULE LIST`](module-list.md) gives it: `search`, `ReJSON`, `timeseries` or `vectorset`. KiviDB loads no other modules; a name that is not one of these gives an empty array.

Names are in lower case. The list is what [`COMMAND COUNT`](command-count.md) counts, with subcommands too.

## Examples

```
> COMMAND LIST FILTERBY ACLCAT hyperloglog
1) "pfadd"
2) "pfcount"
3) "pfmerge"
4) "pfdebug"
5) "pfselftest"
> COMMAND LIST FILTERBY PATTERN client|g*
1) "client|getname"
2) "client|getredir"
> COMMAND LIST FILTERBY MODULE ReJSON
 1) "json.set"
 2) "json.get"
 3) "json.mget"
...
> COMMAND LIST FILTERBY MODULE json
(empty array)
```
