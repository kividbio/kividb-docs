---
title: "HPTTL"
description: "HTTL in milliseconds."
version: "1.2"
command: "HPTTL"
syntax: "HPTTL key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HPTTL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
[`HTTL`](httl.md) in milliseconds.

## Examples

```
> HSET s user ada
(integer) 1
> HPEXPIRE s 5000 FIELDS 1 user
1) (integer) 1
> HPTTL s FIELDS 1 user
1) (integer) 5000
```
