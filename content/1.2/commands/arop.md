---
title: "AROP"
description: "Computes over the filled slots from start to end."
version: "1.2"
command: "AROP"
syntax: "AROP key start end <SUM | MIN | MAX | AND | OR | XOR | MATCH value | USED>"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
AROP key start end <SUM | MIN | MAX | AND | OR | XOR | MATCH value | USED>
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Computes over the filled slots from `start` to `end`.

| Operation | Reply |
|---|---|
| `SUM`, `MIN`, `MAX` | over the numeric values, as a bulk string; `nil` if there are none |
| `AND`, `OR`, `XOR` | of the integer values, as an integer |
| `MATCH value` | how many values equal `value` |
| `USED` | how many slots are filled |

## Examples

```
> ARSET n 0 3 7 hello 10
(integer) 4
> AROP n 0 3 SUM
"20"
> AROP n 0 3 MAX
"10"
> AROP n 0 3 MATCH hello
(integer) 1
> AROP n 2 2 SUM
(nil)
```
