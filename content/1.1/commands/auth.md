---
title: "AUTH"
description: "Logs the connection in as a user: AUTH username password, or, with a password only, as the default user."
version: "1.1"
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

Before logging in, a connection that needs to can only send `AUTH`, `HELLO`, `PING`, `QUIT` and `RESET`; anything else gets `NOAUTH Authentication required.`. That is the case when `requirepass` is set, or the `default` user has a password.

## Reply

- `OK`, as a bulk string, as Redis sends it.
- `WRONGPASS invalid username-password pair or user is disabled.`.

## Differences from Redis

`AUTH password` while the `default` user has no password replies `OK`. Redis refuses it, which tells a client that the password it was given is not in use. Filed as [kividb#135](https://github.com/kividbio/kividb/issues/135).

## Examples

```
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
