---
title: "HDEL"
description: "Deletes fields from the hash at key."
version: "1.2"
command: "HDEL"
syntax: "HDEL key field [field ...]"
group: "hash"
since: "1.1.0"
arity: -3
flags: ["fast", "write"]
acl_categories: ["fast", "hash", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HDEL key field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@hash`, `@write`
<!-- generated: end -->
Deletes fields from the hash at `key`. A hash left with no fields is deleted.

## Reply

- The number of fields deleted; fields that did not exist are not counted.

## Examples

```
> HSET u a 1 b 2
(integer) 2
> HDEL u a b nope
(integer) 2
> EXISTS u
(integer) 0
```
