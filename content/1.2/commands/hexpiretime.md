---
title: "HEXPIRETIME"
description: "Returns the Unix time, in seconds, at which fields of the hash at key expire."
version: "1.2"
command: "HEXPIRETIME"
syntax: "HEXPIRETIME key FIELDS numfields field [field ...]"
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
HEXPIRETIME key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
Returns the Unix time, in seconds, at which fields of the hash at `key` expire.

## Reply

An array with one element per field: the time, `-1` if the field has no expiry, `-2` if there is no such field or key.

## Examples

```
> HSET s token abc
(integer) 1
> HEXPIREAT s 4102444800 FIELDS 1 token
1) (integer) 1
> HEXPIRETIME s FIELDS 1 token
1) (integer) 4102444800
```
