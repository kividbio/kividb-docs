---
title: "ACL SAVE"
description: "Writes every user in memory, with its rules and passwords, to the ACL file, so that they are there after a restart."
version: "1.2"
command: "ACL SAVE"
syntax: "ACL SAVE"
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
ACL SAVE
```

**Available since:** 1.1.0
<!-- generated: end -->
Writes every user in memory, with its rules and passwords, to the ACL file, so that they are there after a restart. Users made or changed with [`ACL SETUSER`](acl-setuser.md) or deleted with [`ACL DELUSER`](acl-deluser.md) live in memory only until `ACL SAVE`: nothing writes the file on its own, at shutdown included.

The file is the one the [`aclfile`](../reference/configuration.md#aclfile) setting names, given at startup (`--aclfile <path>`, or `aclfile` in the config file); `CONFIG SET` cannot change it. The server must have been started with one: it reads the file at startup, and does not start if the file is missing or has an error, so create it, even empty, before the first start.

The file is replaced as a whole: the server writes `<path>.tmp` and renames it over the file, so a crash part way leaves the old file. It writes one `user <name> <rules...>` line per user, `default` first and the others by name, in the form [`ACL LIST`](acl-list.md) prints and [`ACL LOAD`](acl-load.md) reads. Passwords are written as their SHA-256, after `#`, never in clear. Nothing else in a hand-edited file is kept.

Users are not replicated: save on each node, or copy the file to the others and `ACL LOAD` it there. See [Security](../guides/security.md#keeping-users).

## Reply

- `OK`.
- `ERR This KiviDB instance is not configured to use an ACL file. You may want to specify users via the ACL SETUSER command and make sure to also set an aclfile configuration directive.` without an `aclfile`.
- `ERR saving ACL file: <reason>` if the file cannot be written.

## Examples

```
> ACL SETUSER app on >app-password ~app:* +@read +@write -@dangerous
OK
> ACL SAVE
OK
```

The file then holds:

```
user default on nopass ~* &* +@all
user app on #c0741d74e1d41a97476cbf1e058018439fd032d4b3d83e281b705b5547a07077 ~app:* resetchannels -@all +@read +@write -@dangerous
```
