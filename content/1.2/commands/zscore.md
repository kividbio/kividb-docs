---
title: "ZSCORE"
description: "Returns the score of member in the sorted set at key."
version: "1.2"
command: "ZSCORE"
syntax: "ZSCORE key member"
group: "sorted-set"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ZSCORE key member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
Returns the score of `member` in the sorted set at `key`.

## Reply

- The score, as a bulk string.
- `nil` if the member or the key does not exist.

## Examples

```
> ZADD z 7 a
(integer) 1
> ZSCORE z a
"7"
> ZSCORE z nope
(nil)
```
