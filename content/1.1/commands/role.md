---
title: "ROLE"
description: "Returns the server's replication role: master with its offset and replicas, or slave with its master and state."
version: "1.1"
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
Returns the server's replication role: `master` with its offset and replicas, or `slave` with its master and state.

## Examples

```
> ROLE
1) "master"
2) (integer) 0
3) (empty array)
```
