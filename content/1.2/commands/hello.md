---
title: "HELLO"
description: "Switches the connection to RESP2 or RESP3, and returns the server's details: its name, version, protocol, connection ID, mode, role and modules, as a map under RESP3."
version: "1.2"
command: "HELLO"
syntax: "HELLO [protover [AUTH username password] [SETNAME clientname]]"
group: "server"
since: "1.1.0"
arity: -1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HELLO [protover [AUTH username password] [SETNAME clientname]]
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Switches the connection to RESP2 or RESP3, and returns the server's details: its name, version, protocol, connection ID, mode, role and modules, as a map under RESP3. `AUTH username password` logs in first, and `SETNAME name` names the connection; they can come in either order.

`server` and `version` are those of the Redis release KiviDB follows, `redis` and `8.10.0`, as `redis_version` in [`INFO`](info.md); KiviDB's own release follows them, as `kividb_version`. Client libraries that turn their client-side cache on only for Redis 7.4 or later, such as redis-py 8.1 and Jedis 5.2, then do. That is since 1.2.1: 1.2.0 said `server: kividb` and its own version. A tool that tells KiviDB apart by `server` should look for `kividb_version`.

Since 1.2.1 too, as in Redis: a protocol version other than 2 or 3 is `NOPROTO` (1.2.0 took 0 and 1 as 2); `AUTH` without a user name is a syntax error; the protocol changes only once the rest of `HELLO` is accepted (1.2.0 switched to RESP3 even when `AUTH` failed); a failed `AUTH` is written to the [ACL log](acl-log.md); and inside [`MULTI`](multi.md), `HELLO` is queued and takes effect when `EXEC` runs it.

## Reply

- The details.
- `NOPROTO unsupported protocol version` for a number other than 2 or 3; `ERR Protocol version is not an integer or out of range` for one that is not a number.
- `ERR Syntax error in HELLO option 'AUTH'` for `AUTH` without both a user name and a password.
- `NOAUTH`, without `AUTH`, when a password is required.

## Examples

```
> HELLO 3
1# "server" => "redis"
2# "version" => "8.10.0"
3# "kividb_version" => "1.2.1"
4# "proto" => (integer) 3
5# "id" => (integer) 5
6# "mode" => "standalone"
7# "role" => "master"
8# "modules" => ...
> HELLO 1
(error) NOPROTO unsupported protocol version
```
