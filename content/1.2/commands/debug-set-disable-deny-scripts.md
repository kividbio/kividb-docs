---
title: "DEBUG SET-DISABLE-DENY-SCRIPTS"
description: "Accepted, for Redis's test suite, and changes nothing: replies OK for 0 or 1."
version: "1.2"
command: "DEBUG SET-DISABLE-DENY-SCRIPTS"
syntax: "DEBUG SET-DISABLE-DENY-SCRIPTS 0|1"
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
DEBUG SET-DISABLE-DENY-SCRIPTS 0|1
```

**Available since:** 1.2.1
<!-- generated: end -->
Accepted, for Redis's test suite, and changes nothing: replies `OK` for `0` or `1`. In Redis it lets scripts run commands they are otherwise kept from. KiviDB keeps scripts from the same commands either way: see [Scripting](../guides/scripting.md#commands-a-script-cannot-run).

`COMMAND` lists the `DEBUG` subcommands since 1.2.1, so each has a page; before 1.2.1, `DEBUG SET-DISABLE-DENY-SCRIPTS` replied `OK` too. See [`DEBUG`](debug.md).

## Reply

`OK`.

## Examples

```
> DEBUG SET-DISABLE-DENY-SCRIPTS 1
OK
```
