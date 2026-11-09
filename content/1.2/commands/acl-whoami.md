---
title: "ACL WHOAMI"
description: "Returns the name of the user the connection is logged in as."
version: "1.2"
command: "ACL WHOAMI"
syntax: "ACL WHOAMI"
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
ACL WHOAMI
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the name of the user the connection is logged in as. A new connection is logged in as `default`; [`AUTH`](auth.md) with a user name and password, or [`HELLO`](hello.md) with `AUTH`, changes that, and [`RESET`](reset.md) goes back to `default`. Use it to check which user, and so which rights, a connection pool or a client library ended up with.

It takes no arguments. On a server that requires a password, a connection that has not logged in gets `NOAUTH`, as it does for every command but `AUTH`, `HELLO`, `QUIT` and `RESET`.

In KiviDB, `ACL WHOAMI` is in `@admin` and `@dangerous`, as every `ACL` subcommand is; in Redis it is in neither. So a user given `+@all -@dangerous`, as applications often are, is refused it with `NOPERM`. Add `+acl|whoami` to its rules to let it call it. See [Security](../guides/security.md#users).

## Reply

The user name, as a bulk string.

## Examples

```
> ACL WHOAMI
"default"
> AUTH alice alice-pw
OK
> ACL WHOAMI
"alice"
> RESET
RESET
> ACL WHOAMI
"default"
```
