---
title: "ACL USERS"
description: "Returns the names of every user."
version: "1.2"
command: "ACL USERS"
syntax: "ACL USERS"
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
ACL USERS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the names of every user the server has, `default` included, sorted by name. Users that are `off` are listed too. Use it to see who exists; [`ACL LIST`](acl-list.md) shows every user with its rules, and [`ACL GETUSER`](acl-getuser.md) one user in detail.

It takes no arguments. The list is this node's: users are not replicated, and each node of a cluster has its own, unless they share an [`aclfile`](../reference/configuration.md#aclfile).

`ACL USERS` is an administration command, in `@admin` and `@dangerous`, like the rest of `ACL`: a user given only the commands it needs, or `+@all -@dangerous`, is refused it with `NOPERM`. See [Security](../guides/security.md#users).

## Reply

An array of user names, sorted by byte value, so capitals come before lower case.

## Examples

```
> ACL SETUSER alice on >alice-pw ~* +@all
OK
> ACL SETUSER bob off
OK
> ACL USERS
1) "alice"
2) "bob"
3) "default"
> ACL USERS extra
(error) ERR wrong number of arguments for 'acl|users' command
```
