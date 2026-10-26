---
title: "SRANDMEMBER"
description: "Returns members of the set at key, picked at random, without removing them."
version: "1.2"
command: "SRANDMEMBER"
syntax: "SRANDMEMBER key [count]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SRANDMEMBER key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Returns members of the set at `key`, picked at random, without removing them.

## Reply

- Without `count`: a member, or `nil` if the key does not exist.
- With a positive `count`: up to `count` different members.
- With a negative `count`: exactly `-count` members, which may repeat.

## Examples

```
> SADD r 1 2 3
(integer) 3
> SRANDMEMBER r 2
1) "2"
2) "1"
> SRANDMEMBER r -5
1) "3"
2) "3"
3) "3"
4) "2"
5) "3"
```
