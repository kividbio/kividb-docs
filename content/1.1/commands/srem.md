---
title: "SREM"
description: "Removes members from the set at key."
version: "1.1"
command: "SREM"
syntax: "SREM key member [member ...]"
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
SREM key member [member ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@set`, `@write`
<!-- generated: end -->
Removes members from the set at `key`. A set left empty is deleted.

## Reply

- The number of members removed; members not in the set are not counted.

## Examples

```
> SADD s a b
(integer) 2
> SREM s a z
(integer) 1
```
