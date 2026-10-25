---
title: "BITOP"
description: "Combines the strings at the source keys bit by bit and stores the result at destkey."
version: "1.1"
command: "BITOP"
syntax: "BITOP <AND | OR | XOR | NOT> destkey key [key ...]"
group: "bitmap"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["bitmap", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BITOP <AND | OR | XOR | NOT> destkey key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@bitmap`, `@slow`, `@write`
<!-- generated: end -->
Combines the strings at the source keys bit by bit and stores the result at `destkey`. Shorter strings count as padded with zero bytes. A missing key is an empty string.

## Operations

| Operation | Each result bit is set when |
|---|---|
| `AND` | it is set in every key |
| `OR` | it is set in any key |
| `XOR` | it is set in an odd number of keys |
| `NOT` | it is not set in the one key given |
| `DIFF` | it is set in the first key and in none of the others |
| `DIFF1` | it is not set in the first key, but is set in at least one of the others |
| `ANDOR` | it is set in the first key and in at least one of the others |
| `ONE` | it is set in exactly one key |

`NOT` takes exactly one source key; `DIFF`, `DIFF1` and `ANDOR` take at least two. `DIFF`, `DIFF1`, `ANDOR` and `ONE` are the operations Redis 8.2 added.

## Reply

- The length of the string stored at `destkey`, in bytes.

## Examples

```
> SET k1 foof
OK
> SET k2 kook
OK
> BITOP AND d k1 k2
(integer) 4
> GET d
"boob"
> BITOP OR d k1 k2
(integer) 4
> GET d
"oooo"
> BITOP NOT d k1 k2
(error) ERR BITOP NOT must be called with a single source key
```
