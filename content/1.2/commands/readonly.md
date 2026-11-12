---
title: "READONLY"
description: "Lets the connection read from this replica: read commands for the slots of its master are served here, instead of being answered with MOVED."
version: "1.2"
command: "READONLY"
syntax: "READONLY"
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
READONLY
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`

**History:**

- 1.2.1: acl categories: added connection; removed cluster
<!-- generated: end -->
Lets the connection read from this replica: read commands for the slots of its master are served here, instead of being answered with `MOVED`. Writes are still redirected. What a replica returns can be behind its master. [`READWRITE`](readwrite.md) turns it off.

On a server that is not a cluster node it is refused with `ERR This instance has cluster support disabled`, as in Redis, since 1.2.1; before, it answered `OK`. It is in the `@connection` ACL category, as in Redis, since 1.2.1.

## Examples

On a replica:

```
> GET user:7
(error) MOVED 2780 127.0.0.1:17621
> READONLY
OK
> GET user:7
"v"
> SET user:7 w
(error) MOVED 2780 127.0.0.1:17621
```
