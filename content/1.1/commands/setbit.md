---
title: "SETBIT"
description: "Sets or clears the bit at offset in the string at key."
version: "1.1"
command: "SETBIT"
syntax: "SETBIT key offset value"
group: "bitmap"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SETBIT key offset value
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
Sets or clears the bit at `offset` in the string at `key`. Offset `0` is the most significant bit of the first byte. The string grows, with zero bytes, if it is shorter; a missing key is created.

## Reply

- The bit's value before: `0` or `1`.

## Examples

```
> SETBIT b 7 1
(integer) 0
> SETBIT b 7 0
(integer) 1
```
