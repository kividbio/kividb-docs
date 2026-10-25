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
acl_categories: ["cluster", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
READONLY
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@fast`
<!-- generated: end -->
Lets the connection read from this replica: read commands for the slots of its master are served here, instead of being answered with `MOVED`. Writes are still redirected. What a replica returns can be behind its master. [`READWRITE`](readwrite.md) turns it off.

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
