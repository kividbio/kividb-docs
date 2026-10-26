---
title: "ARSET"
description: "Sets values in the array at key from index on, one slot each."
version: "1.1"
command: "ARSET"
syntax: "ARSET key index value [value ...]"
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
ARSET key index value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Sets values in the array at `key` from `index` on, one slot each. An array is sparse: slots are addressed by index, from 0, and only filled ones take memory. A missing key is created. Arrays are Redis 8.8's type; `TYPE` reports `array`.

## Reply

- The number of slots that were empty and are now filled.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARSET a 5 w
(integer) 1
> TYPE a
array
```
