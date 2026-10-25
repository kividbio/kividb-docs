---
title: "XREVRANGE"
description: "XRANGE, newest first; end comes first."
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
[`XRANGE`](xrange.md), newest first; `end` comes first.

## Examples

```
> XADD s 1-0 t 1
"1-0"
> XADD s 2-0 t 2
"2-0"
> XREVRANGE s + - COUNT 1
1) 1) "2-0"
   2) 1) "t"
      2) "2"
```
