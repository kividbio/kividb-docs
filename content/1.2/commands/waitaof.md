---
title: "WAITAOF"
description: "Waits until every write this connection made before it is in the local AOF and fsynced (numlocal), and in numreplicas replicas' AOFs, or timeout milliseconds pass."
version: "1.2"
command: "WAITAOF"
syntax: "WAITAOF numlocal numreplicas timeout"
group: "server"
since: "1.1.0"
arity: 4
flags: ["blocking"]
acl_categories: ["blocking", "generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
WAITAOF numlocal numreplicas timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
Waits until every write this connection made before it is in the local AOF and fsynced (`numlocal`), and in `numreplicas` replicas' AOFs, or `timeout` milliseconds pass.

## Reply

- An array: the number of local fsyncs, `0` or `1`, and the number of replicas.

## Known issue

With the AOF off, `WAITAOF` replies that the local fsync happened, `[1, 0]`; Redis refuses `numlocal` without an AOF. Do not rely on `WAITAOF` for durability unless `appendonly` is `yes`. Filed as [kividb#137](https://github.com/kividbio/kividb/issues/137).
