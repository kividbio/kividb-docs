---
title: "ZINCRBY"
description: "Adds increment to the score of member in the sorted set at key."
version: "1.2"
command: "ZINCRBY"
syntax: "ZINCRBY key increment member"
group: "sorted-set"
since: "1.1.0"
arity: 4
flags: ["fast", "write"]
acl_categories: ["fast", "sortedset", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZINCRBY key increment member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@sortedset`, `@write`
<!-- generated: end -->
Adds `increment` to the score of `member` in the sorted set at `key`. A missing member is added with `increment` as its score.

## Reply

- The new score, as a bulk string.

## Examples

```
> ZADD z 2 b
(integer) 1
> ZINCRBY z 2.5 b
"4.5"
> ZINCRBY z 1 new
"1"
```
