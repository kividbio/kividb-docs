---
title: "ACL DELUSER"
description: "Deletes one or more users."
version: "1.2"
command: "ACL DELUSER"
syntax: "ACL DELUSER username [username ...]"
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
ACL DELUSER username [username ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes one or more users. Every connection logged in as a deleted user is closed at once, so a user's access ends with this command, not with its next login. Use [`ACL SETUSER name off`](acl-setuser.md) instead to keep the user and its rules while nobody can use it.

- `username [username ...]`: the users to delete. A name that is not a user is skipped, and not counted.

The `default` user cannot be deleted. If it is among the names, nothing is deleted, the other users included.

The change is in memory only. With an [`aclfile`](../reference/configuration.md#aclfile), [`ACL SAVE`](acl-save.md) writes it to the file; until then, a restart or an [`ACL LOAD`](acl-load.md) brings back the users the file has. Users are not replicated: delete the user on every node. See [Security](../guides/security.md#keeping-users).

## Reply

- The number of users deleted.
- `ERR The 'default' user cannot be removed` if `default` is named.

## Examples

```
> ACL SETUSER alice
OK
> ACL SETUSER bob on >pw ~* +@all
OK
> ACL DELUSER bob nobody
(integer) 1
> ACL DELUSER alice default
(error) ERR The 'default' user cannot be removed
> ACL USERS
1) "alice"
2) "default"
```
