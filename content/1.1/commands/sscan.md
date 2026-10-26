---
title: "SSCAN"
description: "Goes through the members of the set at key a page at a time, as SCAN goes through keys."
version: "1.1"
command: "SSCAN"
syntax: "SSCAN key cursor [MATCH pattern] [COUNT count]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SSCAN key cursor [MATCH pattern] [COUNT count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
Goes through the members of the set at `key` a page at a time, as [`SCAN`](scan.md) goes through keys. Start with cursor `0`, and call again with the cursor each reply gives, until it gives `0`.

## Options

| Option | Effect |
|---|---|
| `MATCH pattern` | Return only members matching a glob-style pattern. |
| `COUNT count` | How many members to look at a call: a hint. |

## Reply

- A two-element array: the next cursor, and the members of this page.

## Examples

```
> SADD x b c d
(integer) 3
> SSCAN x 0
1) "0"
2) 1) "d"
   2) "c"
   3) "b"
> SSCAN x 0 MATCH b*
1) "0"
2) 1) "b"
```
