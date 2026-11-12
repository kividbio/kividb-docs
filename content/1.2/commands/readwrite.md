---
title: "READWRITE"
description: "Turns off READONLY for the connection."
version: "1.2"
command: "READWRITE"
syntax: "READWRITE"
group: "cluster"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: [{"release": "1.2.1", "change": "acl categories: added connection; removed cluster"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
READWRITE
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`

**History:**

- 1.2.1: acl categories: added connection; removed cluster
<!-- generated: end -->
Turns off [`READONLY`](readonly.md) for the connection. After it, a replica answers reads for its master's slots with `MOVED` again, sending the client to the master, as it does for writes.

It lasts for the connection, until the next `READONLY`, and it is the state every connection starts in, so sending it to a connection that never sent `READONLY` changes nothing. On a master it changes nothing either: a master serves its own slots either way. See [Reading from replicas](../guides/cluster.md#reading-from-replicas).

A server that is not a cluster node replies `ERR This instance has cluster support disabled`, as Redis does, since 1.2.1; 1.2.0 answered `OK`.

## Reply

`OK`, or `ERR This instance has cluster support disabled` on a server that is not a cluster node.

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
