---
title: "HPEXPIRE"
description: "HEXPIRE with the time in milliseconds."
version: "1.2"
command: "HPEXPIRE"
syntax: "HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -6
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HPEXPIRE key milliseconds [NX | XX | GT | LT] FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
[`HEXPIRE`](hexpire.md) with the time in milliseconds.

## Examples

```
> HSET s user ada
(integer) 1
> HPEXPIRE s 5000 FIELDS 1 user
1) (integer) 1
> HPTTL s FIELDS 1 user
1) (integer) 5000
```
