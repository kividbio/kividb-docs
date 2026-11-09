---
title: "ACL HELP"
description: "Lists the ACL subcommands and what each does."
version: "1.2"
command: "ACL HELP"
syntax: "ACL HELP"
group: "acl"
since: "1.1.0"
history: []
container: "ACL"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ACL HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `ACL` subcommands, each with its arguments and a line on what it does, as the server knows them. It is the quick reminder from inside a client; the [`ACL`](acl.md) page links to each subcommand's own page, and [Security](../guides/security.md#users) explains users and their rules.

It takes no arguments. Before 1.2, KiviDB did not have `ACL HELP`, though its error for an unknown subcommand said to try it: `ERR unknown subcommand 'HELP'. Try ACL HELP.` That error still ends the same way, and now leads somewhere.

## Reply

An array of strings: a heading, then, for each subcommand, its syntax and an indented description.

## Examples

```
> ACL HELP
 1) ACL <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) CAT [<category>]
 3)     List all commands that belong to <category>, or all command categories
 4) DELUSER <username> [<username> ...]
 5)     Delete a list of users.
 6) DRYRUN <username> <command> [<arg> ...]
 7)     Returns whether the user can execute the given command without executing the command.
...
22) USERS
23)     List all the registered usernames.
24) WHOAMI
25)     Return the current connection username.
26) HELP
27)     Print this help.
> ACL NOPE
(error) ERR unknown subcommand 'NOPE'. Try ACL HELP.
```
