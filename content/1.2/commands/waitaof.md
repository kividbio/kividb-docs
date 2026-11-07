---
title: "WAITAOF"
description: "Waits for pending writes to be fsynced to the local append-only file, or until timeout milliseconds pass."
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
Waits for pending writes to be fsynced to the local append-only file, or until `timeout` milliseconds pass.

In 1.2, `numreplicas` is accepted but ignored: KiviDB does not track replicas' AOF fsync acknowledgements, and the second number in the reply is always `0`. The timeout applies only to the local fsync; the command does not wait for replicas. [`WAIT`](wait.md) can wait for replication acknowledgements, but those do not confirm that a replica has fsynced its AOF.

## Reply

- A two-element array: the local fsync status, `0` or `1`, followed by `0` for replicas. With the AOF on, the first is `1` once the writes are fsynced, whatever `numlocal` asked for, as in Redis.
- `ERR WAITAOF cannot be used when numlocal is set but appendonly is disabled.`, with the AOF off and `numlocal` above 0. `WAITAOF 0 ...` then replies `[0, 0]`.

Before 1.2, with the AOF off, it replied `[1, 0]`, as if the writes had been fsynced, and with the AOF on, the first number was `0` for `numlocal` 0.

## Examples

```
> WAITAOF 1 0 0
(error) ERR WAITAOF cannot be used when numlocal is set but appendonly is disabled.
> CONFIG SET appendonly yes
OK
> SET a 1
OK
> WAITAOF 1 0 0
1) (integer) 1
2) (integer) 0
> WAITAOF 1 1 10000
1) (integer) 1
2) (integer) 0
```

The last call returns once the local fsync completes, even without a replica; it does not wait ten seconds for one.
