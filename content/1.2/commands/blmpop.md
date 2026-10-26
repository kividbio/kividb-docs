---
title: "BLMPOP"
description: "LMPOP that waits until one of the lists has an element, or timeout seconds have passed."
version: "1.2"
command: "BLMPOP"
syntax: "BLMPOP timeout numkeys key [key ...] LEFT|RIGHT [COUNT count]"
group: "list"
since: "1.1.0"
arity: -5
flags: ["blocking", "movablekeys", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BLMPOP timeout numkeys key [key ...] LEFT|RIGHT [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
[`LMPOP`](lmpop.md) that waits until one of the lists has an element, or `timeout` seconds have passed.

## Reply

- A two-element array: the key popped from, and the elements.
- `nil` if the timeout passed.

## Examples

```
> RPUSH b2 1 2
(integer) 2
> BLMPOP 1 2 b0 b2 LEFT COUNT 3
1) "b2"
2) 1) "1"
   2) "2"
```
