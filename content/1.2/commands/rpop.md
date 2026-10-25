---
title: "RPOP"
description: "Removes and returns the last element of the list at key."
version: "1.2"
command: "RPOP"
syntax: "RPOP key [count]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "list", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RPOP key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Removes and returns the last element of the list at `key`. With `count`, removes and returns up to that many, last first. A list left empty is deleted.

## Reply

- The element, or `nil` if the key does not exist.
- With `count`: an array of up to `count` elements, or `nil` if the key does not exist.

## Examples

```
> RPUSH l a b c
(integer) 3
> RPOP l
"c"
> RPOP l 5
1) "b"
2) "a"
```
