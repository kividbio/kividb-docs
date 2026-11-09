---
title: "XREVRANGE"
description: "Returns the entries of the stream at key from end down to start, newest first: XRANGE in reverse, with the two bounds given the other way round."
version: "1.2"
command: "XREVRANGE"
syntax: "XREVRANGE key end start [COUNT count]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XREVRANGE key end start [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
Returns the entries of the stream at `key` from `end` down to `start`, newest first: [`XRANGE`](xrange.md) in reverse, with the two bounds given the other way round. Use it for the latest entries, such as the last few events of a log: `XREVRANGE key + - COUNT 10`.

- `end`, `start`: IDs, both included. `+` is the newest entry and `-` the oldest. `(` before an ID excludes it, and an ID without a sequence number, `1`, covers that whole millisecond.
- `COUNT count`: at most `count` entries. To page backwards, pass the last ID returned, with `(`, as the next `end`.

Bounds given in `XRANGE`'s order, `-` before `+`, match nothing.

## Reply

- An array of entries, newest first, each an array of its ID and its field-value pairs.
- An empty array if no entry is in the range, or the key does not exist.
- `WRONGTYPE` if the key holds another type; `ERR Invalid stream ID specified as stream command argument` for a bound that is not an ID.

## Examples

```
> XADD s 1-1 temp 20
"1-1"
> XADD s 1-2 temp 21
"1-2"
> XADD s 2-0 temp 22
"2-0"
> XREVRANGE s + - COUNT 1
1) 1) "2-0"
   2) 1) "temp"
      2) "22"
> XREVRANGE s (2-0 - COUNT 1
1) 1) "1-2"
   2) 1) "temp"
      2) "21"
> XREVRANGE s 1 1
1) 1) "1-2"
   2) 1) "temp"
      2) "21"
2) 1) "1-1"
   2) 1) "temp"
      2) "20"
> XREVRANGE s - +
(empty array)
```
