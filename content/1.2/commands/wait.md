---
title: "WAIT"
description: "Waits until numreplicas replicas have acknowledged every write this connection made before it, or timeout milliseconds pass; 0 waits for ever."
version: "1.2"
command: "WAIT"
syntax: "WAIT numreplicas timeout"
group: "server"
since: "1.1.0"
arity: 3
flags: ["blocking"]
acl_categories: ["blocking", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
WAIT numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Waits until `numreplicas` replicas have acknowledged every write this connection made before it, or `timeout` milliseconds pass; `0` waits for ever.

## Reply

- The number of replicas that acknowledged.

## Examples

```
> WAIT 0 100
(integer) 0
```
