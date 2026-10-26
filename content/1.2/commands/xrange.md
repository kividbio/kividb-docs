---
title: "XRANGE"
description: "Returns the entries of the stream at key with IDs from start to end, both included, oldest first."
version: "1.2"
command: "XRANGE"
syntax: "XRANGE key start end [COUNT count]"
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
XRANGE key start end [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
Returns the entries of the stream at `key` with IDs from `start` to `end`, both included, oldest first. `-` and `+` are the stream's ends; `(` before an ID excludes it; an ID without a sequence, `1`, covers that whole millisecond. `COUNT count` returns at most `count` entries.

## Reply

- An array of entries, each an array of its ID and its field-value pairs.

## Examples

```
> XADD s 1-1 temp 20
"1-1"
> XADD s 1-2 temp 21
"1-2"
> XADD s 2-0 temp 22
"2-0"
> XRANGE s 1 1
1) 1) "1-1"
   2) 1) "temp"
      2) "20"
2) 1) "1-2"
   2) 1) "temp"
      2) "21"
> XRANGE s (1-2 + COUNT 1
1) 1) "2-0"
   2) 1) "temp"
      2) "22"
```
