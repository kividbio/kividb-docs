---
title: "LPOP"
description: "Removes and returns the first element of the list at key."
version: "1.1"
command: "LPOP"
syntax: "LPOP key [count]"
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
LPOP key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@list`, `@write`
<!-- generated: end -->
Removes and returns the first element of the list at `key`. With `count`, removes and returns up to that many. A list left empty is deleted.

## Reply

- The element, or `nil` if the key does not exist.
- With `count`: an array of up to `count` elements, or `nil` if the key does not exist.

## Examples

```
> RPUSH l a b c
(integer) 3
> LPOP l
"a"
> LPOP l 5
1) "b"
2) "c"
> EXISTS l
(integer) 0
```
