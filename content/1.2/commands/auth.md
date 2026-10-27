---
title: "AUTH"
description: "Logs the connection in as a user: AUTH username password, or, with a password only, as the default user."
version: "1.2"
command: "AUTH"
syntax: "AUTH [username] password"
group: "acl"
since: "1.1.0"
arity: -2
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
AUTH [username] password
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Logs the connection in as a user: `AUTH username password`, or, with a password only, as the `default` user.

Before logging in, a connection that needs to can only send `AUTH`, `HELLO` with `AUTH`, `QUIT` and `RESET`; anything else gets `NOAUTH Authentication required.`. That is the case when `requirepass` is set, or the `default` user has a password.

While the `default` user has no password, `AUTH password` is refused, as in Redis: a client learns that the password it was given is not in use. `AUTH default password` still logs in. Before 1.2, `AUTH password` replied `OK`.

## Reply

- `OK`, as a bulk string, as Redis sends it.
- `WRONGPASS invalid username-password pair or user is disabled.`.
- `ERR AUTH <password> called without any password configured for the default user. Are you sure your configuration is correct?` for a password alone, while the `default` user has none.

## Examples

```
> AUTH somepassword
(error) ERR AUTH <password> called without any password configured for the default user. Are you sure your configuration is correct?
> AUTH alice wrong
(error) WRONGPASS invalid username-password pair or user is disabled.
> AUTH alice s3cret
OK
> CONFIG SET requirepass topsecret
OK
```

On a new connection:

```
> GET x
(error) NOAUTH Authentication required.
> AUTH topsecret
OK
```
