---
title: "ARSEEK"
description: "Moves the insert cursor to index."
version: "1.1"
command: "ARSEEK"
syntax: "ARSEEK key index"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARSEEK key index
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Moves the insert cursor to `index`. It does not create the key.

## Reply

- `1` if the cursor moved, `0` if the key does not exist.

## Examples

```
> ARSEEK log 10
(integer) 1
> ARINSERT log at10
(integer) 10
```
