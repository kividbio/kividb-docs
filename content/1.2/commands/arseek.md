---
title: "ARSEEK"
description: "Moves the insert cursor to index."
version: "1.2"
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
Moves the insert cursor of the array at `key` to `index`, so the next [`ARINSERT`](arinsert.md) writes there. Use it to rewind a log and write over old entries, or to start inserting at a chosen position. [`ARNEXT`](arnext.md) reads where the cursor is.

`ARSEEK` does not create the key: on a missing key it replies `0` and does nothing. It does not change any value, and a slot the cursor reaches that is already filled is overwritten by the next `ARINSERT`.

`index` is a whole number from `0` to 18446744073709551615. A cursor past 9223372036854775807, the last index, leaves nowhere to insert: `ARNEXT` then gives `nil`. Moving the cursor of an array with no filled slots back to `0` deletes the key, as nothing then sets it apart from a missing one.

## Reply

- `1` if the cursor moved.
- `0` if the key does not exist.

## Errors

- `ERR invalid array index` for an index that is negative, not a whole number or too large.
- `WRONGTYPE` if the key holds a value that is not an array.

## Examples

```
> ARSEEK log 10
(integer) 0
> ARINSERT log first second
(integer) 1
> ARSEEK log 10
(integer) 1
> ARINSERT log at10
(integer) 10
> ARSEEK log 0
(integer) 1
> ARINSERT log again
(integer) 0
> ARMGET log 0 1 10
1) "again"
2) "second"
3) "at10"
```
