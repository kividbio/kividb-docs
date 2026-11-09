---
title: "ROLE"
description: "Returns the server's replication role, with what a client needs to know about it, in fewer bytes than INFO replication."
version: "1.2"
command: "ROLE"
syntax: "ROLE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["dangerous", "fast", "server"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ROLE
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@fast`, `@server`
<!-- generated: end -->
Returns the server's replication role, with what a client needs to know about it, in fewer bytes than [`INFO replication`](info.md). Clients and failover tools use it to tell a master from a replica.

- A master: `master`, its replication offset, and an entry per replica with its address, port and the offset it has acknowledged.
- A replica: `slave`, its master's address and port, the state of its link (`connect`, `connecting`, `sync` or `connected`), and the offset it has received.

## Examples

On a master with one replica:

```
> ROLE
1) "master"
2) (integer) 64
3) 1) 1) "127.0.0.1"
      2) "6391"
      3) "64"
```

On the replica:

```
> ROLE
1) "slave"
2) "127.0.0.1"
3) (integer) 6390
4) "connected"
5) (integer) 64
```
