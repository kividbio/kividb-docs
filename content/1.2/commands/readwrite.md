---
title: "READWRITE"
description: "Turns off READONLY for the connection: reads on a replica are redirected to the master again."
version: "1.2"
command: "READWRITE"
syntax: "READWRITE"
group: "cluster"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["cluster", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
READWRITE
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@fast`
<!-- generated: end -->
Turns off [`READONLY`](readonly.md) for the connection. After it, a replica answers reads for its master's slots with `MOVED` again, sending the client to the master, as it does for writes.

It lasts for the connection, until the next `READONLY`, and it is the state every connection starts in, so sending it to a connection that never sent `READONLY` changes nothing. On a master it changes nothing either: a master serves its own slots either way. See [Reading from replicas](../guides/cluster.md#reading-from-replicas).

Unlike Redis, a server that is not a cluster node also answers `OK`, where Redis replies `ERR This instance has cluster support disabled`.

## Reply

`OK`.

## Examples

On a replica of the master that owns slot 2780:

```
> READONLY
OK
> GET user:7
"v"
> READWRITE
OK
> GET user:7
(error) MOVED 2780 127.0.0.1:7100
```
