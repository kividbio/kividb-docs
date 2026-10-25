---
title: "LTRIM"
description: "Keeps only the elements from index start to index stop, both included, and removes the rest."
version: "1.1"
command: "LTRIM"
syntax: "LTRIM key start stop"
group: "list"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LTRIM key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
Keeps only the elements from index `start` to index `stop`, both included, and removes the rest. Negative indexes count from the end. A range outside the list leaves it empty, and the key is deleted.

## Reply

- `OK`.

## Examples

```
> RPUSH t a b c d e
(integer) 5
> LTRIM t 1 3
OK
> LRANGE t 0 -1
1) "b"
2) "c"
3) "d"
```
