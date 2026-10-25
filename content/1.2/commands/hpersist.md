---
title: "HPERSIST"
description: "Removes the expiry of fields of the hash at key."
version: "1.2"
command: "HPERSIST"
syntax: "HPERSIST key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["hash", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HPERSIST key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@slow`, `@write`
<!-- generated: end -->
Removes the expiry of fields of the hash at `key`.

## Reply

An array with one element per field:
- `1`: the expiry was removed;
- `-1`: the field had none;
- `-2`: no such field, or no such key.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HEXPIRE s 100 FIELDS 2 token user
1) (integer) 1
2) (integer) 1
> HPERSIST s FIELDS 3 token user nope
1) (integer) 1
2) (integer) 1
3) (integer) -2
```
