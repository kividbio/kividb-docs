---
title: "ACL SETUSER"
description: "Creates the user username, or changes it, by applying rules from left to right."
version: "1.1"
command: "ACL SETUSER"
syntax: "ACL SETUSER"
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
ACL SETUSER
```

**Available since:** 1.1.0
<!-- generated: end -->
Creates the user `username`, or changes it, by applying rules from left to right. A user that does not exist starts with no permissions, disabled.

## Rules

| Rule | Effect |
|---|---|
| `on`, `off` | Enable or disable the user. A disabled user cannot log in. |
| `>password`, `<password` | Add or remove a password. A user can have several. |
| `#sha256`, `!sha256` | Add or remove a password by its SHA-256 hash. |
| `nopass`, `resetpass` | Allow any password, or remove every password. |
| `+command`, `-command` | Allow or deny a command; `command\|subcommand` for one subcommand. |
| `+@category`, `-@category` | Allow or deny a category of commands; [`ACL CAT`](acl-cat.md) lists them. `+@all` and `-@all` are every command. |
| `~pattern` | Allow reading and writing keys matching a glob-style pattern; `~*` or `allkeys` for all. |
| `%R~pattern`, `%W~pattern`, `%RW~pattern` | Allow only reading, only writing, or both, for matching keys. |
| `&pattern` | Allow publishing and subscribing to matching channels; `allchannels` for all. A user with none cannot use pub/sub. |
| `resetkeys`, `resetchannels` | Remove every key, or channel, pattern. |
| `reset` | Back to a new user's state. |

Command rules apply in order, so the last one that names a command decides for it: `-@all +get +set` allows only `GET` and `SET`. With an ACL file configured (`aclfile`), the change is saved to it at once.

## Reply

- `OK`.
- `ERR Error in ACL SETUSER modifier '...': Syntax error` for a rule that is not one; nothing changes.

## Examples

```
> ACL SETUSER alice on >s3cret ~cache:* &news -@all +get +set
OK
> ACL SETUSER bob on >pw %R~* -@all +@read
OK
> ACL SETUSER dave nosuchrule
(error) ERR Error in ACL SETUSER modifier 'nosuchrule': Syntax error
```

Then, logged in as alice:

```
> AUTH alice s3cret
OK
> SET cache:1 v
OK
> SET other v
(error) NOPERM User alice has no permissions to access the 'other' key
> DEL cache:1
(error) NOPERM User alice has no permissions to run the 'del' command
```
