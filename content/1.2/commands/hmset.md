---
title: "HMSET"
description: "Another name for HSET, kept for old clients."
version: "1.2"
command: "HMSET"
syntax: "HMSET key field value [field value ...]"
group: "hash"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HMSET key field value [field value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Another name for [`HSET`](hset.md), kept for old clients. It replies `OK` instead of a count.

## Examples

```
> HMSET u a 1 b 2
OK
```
