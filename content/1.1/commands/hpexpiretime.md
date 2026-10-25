---
title: "HPEXPIRETIME"
description: "HEXPIRETIME in milliseconds."
version: "1.1"
command: "HPEXPIRETIME"
syntax: "HPEXPIRETIME key FIELDS numfields field [field ...]"
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
HPEXPIRETIME key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
[`HEXPIRETIME`](hexpiretime.md) in milliseconds.

## Examples

```
> HSET s token abc
(integer) 1
> HEXPIREAT s 4102444800 FIELDS 1 token
1) (integer) 1
> HPEXPIRETIME s FIELDS 1 token
1) (integer) 4102444800000
```
