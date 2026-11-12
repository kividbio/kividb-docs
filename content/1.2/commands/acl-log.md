---
title: "ACL LOG"
description: "Returns recent security events, newest first: failed logins, and commands, keys or channels refused for lack of permission."
version: "1.2"
command: "ACL LOG"
syntax: "ACL LOG [count | RESET]"
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
ACL LOG [count | RESET]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns recent security events, newest first: failed logins, and commands, keys or channels refused for lack of permission. Each event has, in Redis's order, `count`, `reason` (`auth`, `command`, `key` or `channel`), `context` (`toplevel`, `multi` or `lua`), `object` (the command, key or channel refused; `AUTH` or `HELLO` for a failed login), `username`, `age-seconds`, `client-info` (as [`CLIENT INFO`](client-info.md) gives it), `entry-id`, `timestamp-created` and `timestamp-last-updated`. Under RESP3 each event is a map.

Without `count`, the ten newest events are returned; `count` returns at most that many, and a negative one none. `RESET` empties the log. The log keeps the [`acllog-max-len`](../reference/configuration.md#acllog-max-len) newest events (128). An event like one of the ten newest, with the same reason, context, object and user within 60 seconds, adds to that entry's `count` and moves its `timestamp-last-updated`, rather than adding an entry. A command refused for want of `AUTH` is not logged.

That is as in Redis, since 1.2.1. In 1.2.0, the fields came in another order, the entry's number was `id` and counted from 1, `ACL LOG` without a count returned every entry, every refusal said `toplevel`, a failed login's object was the user name, and `acllog-max-len` was accepted and ignored. A client that reads entries by position, or by the name `id`, needs to change.

## Examples

After a client tried to log in as `carol` with a wrong password:

```
> ACL LOG 1
1)  1) "count"
    2) (integer) 1
    3) "reason"
    4) "auth"
    5) "context"
    6) "toplevel"
    7) "object"
    8) "AUTH"
    9) "username"
   10) "carol"
   11) "age-seconds"
   12) "0.005"
   13) "client-info"
   14) "id=274 addr=127.0.0.1:38210 laddr=127.0.0.1:6380 fd=0 name= age=0 idle=0 flags=N db=0 ..."
   15) "entry-id"
   16) (integer) 0
   17) "timestamp-created"
   18) (integer) 1794480298485
   19) "timestamp-last-updated"
   20) (integer) 1794480298485
> ACL LOG RESET
OK
```
