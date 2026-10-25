---
title: "SADD"
description: "Adds members to the set at key."
version: "1.1"
command: "SADD"
syntax: "SADD key member [member ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "set", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SADD key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
Adds members to the set at `key`. Members already in the set are skipped. A missing key is created.

## Reply

- The number of members added.
- A `WRONGTYPE` error if the key is not a set.

## Examples

```
> SADD s a b c
(integer) 3
> SADD s a d
(integer) 1
```
