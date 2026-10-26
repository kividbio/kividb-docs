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
Turns off [`READONLY`](readonly.md) for the connection: reads on a replica are redirected to the master again.

## Examples

```
> READWRITE
OK
```
