---
title: "ACL LOAD"
description: "Replaces every user with those in the ACL file, the aclfile setting."
version: "1.2"
command: "ACL LOAD"
syntax: "ACL LOAD"
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
ACL LOAD
```

**Available since:** 1.1.0
<!-- generated: end -->
Reads the ACL file again and makes its users the server's users, replacing all of those in memory. Use it after editing the file by hand, or after copying one in from another node, to apply it without a restart. The file is the one the [`aclfile`](../reference/configuration.md#aclfile) setting names, given at startup (`--aclfile <path>`, or `aclfile` in the config file); `CONFIG SET` cannot change it.

The file has one line per user, `user <name> <rules...>`, in the form [`ACL LIST`](acl-list.md) prints and [`ACL SAVE`](acl-save.md) writes. Loading is all or nothing:

- A file with an error, a line that does not start with `user`, an unknown rule or category, or a user named twice, changes nothing, and the error names the line.
- Otherwise the file is what the users now are. A user not in it is deleted, and its connections are closed. A user in it gets the file's rules and passwords, and connections logged in as it stay open under the new rules. A password no longer in the file no longer works.
- If the file has no `default` user, `default` is reset to one that may run everything, with no password (or the [`requirepass`](../reference/configuration.md#requirepass) password, if one is set).

A server started with an `aclfile` that does not exist, or has an error, does not start. Users are not replicated: give every node the same file. See [Security](../guides/security.md#keeping-users).

## Reply

- `OK`.
- `ERR This KiviDB instance is not configured to use an ACL file` without an `aclfile`.
- `ERR <path>: line <n>: <what is wrong>. WARNING: ACL errors detected, no change to the previously active ACL rules was performed` if the file has an error.

## Examples

```
> ACL LOAD
OK
> ACL LOAD
(error) ERR /etc/kividb/users.acl: line 2: error in rule '+@nosuchcat': Unknown command or category name in ACL. WARNING: ACL errors detected, no change to the previously active ACL rules was performed
```

On a server started without an `aclfile`:

```
> ACL LOAD
(error) ERR This KiviDB instance is not configured to use an ACL file
```
