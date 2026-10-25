---
title: "HTTL"
description: "Returns how long fields of the hash at key have before they expire, in seconds."
version: "1.2"
command: "HTTL"
syntax: "HTTL key FIELDS numfields field [field ...]"
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
HTTL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns how long fields of the hash at `key` have before they expire, in seconds.

## Reply

An array with one element per field:
- the seconds left;
- `-1`: the field has no expiry;
- `-2`: no such field, or no such key.

## Examples

```
> HSET s token abc user ada
(integer) 2
> HEXPIRE s 100 FIELDS 1 token
1) (integer) 1
> HTTL s FIELDS 3 token user nope
1) (integer) 100
2) (integer) -1
3) (integer) -2
```
