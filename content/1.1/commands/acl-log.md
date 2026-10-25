---
title: "ACL LOG"
description: "Returns recent security events, newest first: failed logins, and commands, keys or channels refused for lack of permission."
version: "1.1"
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
Returns recent security events, newest first: failed logins, and commands, keys or channels refused for lack of permission. Each event has its reason, the user, the object refused, the client, and how many times it happened. `count` returns at most that many; `RESET` empties the log.

## Examples

```
> ACL LOG 1
1)  1) "id"
    2) (integer) 8
    ...
    9) "reason"
   10) "auth"
   ...
   13) "object"
   14) "carol"
   15) "username"
   16) "carol"
   ...
> ACL LOG RESET
OK
```
