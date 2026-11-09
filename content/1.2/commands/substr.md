---
title: "SUBSTR"
description: "Another name for GETRANGE, kept for old clients."
version: "1.2"
command: "SUBSTR"
syntax: "SUBSTR key start stop"
group: "string"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUBSTR key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
Returns part of the string at `key`, from byte offset `start` to byte offset `stop`, both included. It is the old name of [`GETRANGE`](getrange.md), kept so that old clients work; it takes the same arguments and gives the same replies. New code should use `GETRANGE`.

- Offsets count bytes from `0`. Negative offsets count from the end: `-1` is the last byte.
- A range past the end is cut to the end of the string; a range that ends before it starts returns an empty string.
- A key that does not exist returns an empty string, not `nil`.
- A number stored as a string is read as its digits.

## Reply

The bytes in the range, as a bulk string.

## Errors

- `WRONGTYPE`: `key` holds something other than a string.
- `ERR value is not an integer or out of range`: an offset is not an integer.

## Examples

```
> SET k "hello world"
OK
> SUBSTR k 0 4
"hello"
> SUBSTR k -5 -1
"world"
> SUBSTR k 6 100
"world"
> SUBSTR k 5 2
""
> SUBSTR nokey 0 4
""
```
