---
title: "ARMSET"
description: "Sets values at several indexes in the array at key, in one call."
version: "1.2"
command: "ARMSET"
syntax: "ARMSET key index value [index value ...]"
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
ARMSET key index value [index value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Sets values at several indexes in the array at `key`, in one call. Each `index value` pair writes one slot; the indexes can be in any order and need not be next to each other. A missing key is created. For values at consecutive indexes, [`ARSET`](arset.md) takes one starting index and a list of values.

Indexes are whole numbers from `0`. Every pair is checked before any slot is written, so a bad index anywhere leaves the array unchanged. If the same index appears twice, the later value wins. `ARMSET` does not move the insert cursor that [`ARINSERT`](arinsert.md) uses.

## Reply

- The number of slots that were empty and are now filled, as an integer. Overwriting a filled slot is not counted.

## Errors

- `ERR invalid array index` for an index that is negative or not a whole number.
- `ERR wrong number of arguments for 'armset' command` when the last index has no value.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSET a 0 x y z
(integer) 3
> ARMSET a 3 m 9 n
(integer) 2
> ARMSET a 3 mm 10 o
(integer) 1
> ARMGET a 3 9 10
1) "mm"
2) "n"
3) "o"
> ARMSET a 1 b -2 c
(error) ERR invalid array index
> ARGET a 1
"y"
```
