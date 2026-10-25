---
title: "FT.CURSOR READ"
description: "Returns the next rows of an aggregation started with WITHCURSOR, COUNT n at a time, and the cursor to read on with: 0 once there are no more, and the cursor is closed."
version: "1.1"
command: "FT.CURSOR READ"
syntax: "FT.CURSOR READ index cursor_id [COUNT n]"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CURSOR"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CURSOR READ index cursor_id [COUNT n]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the next rows of an aggregation started with `WITHCURSOR`, `COUNT n` at a time, and the cursor to read on with: `0` once there are no more, and the cursor is closed. A cursor holds the results as they were when the aggregation ran. It is dropped after `MAXIDLE` unread, and when its index is.

## Examples

```
> FT.AGGREGATE products * LOAD 1 @name WITHCURSOR COUNT 2
1) 1) (integer) 2
   2) 1) "name"
      2) "Wireless keyboard"
   3) 1) "name"
      2) "USB-C cable, 2 m"
2) (integer) 2066851009692363303
> FT.CURSOR READ products 2066851009692363303
1) 1) (integer) 2
   2) 1) "name"
      2) "Desk lamp with USB port"
   3) 1) "name"
      2) "Oak desk"
2) (integer) 0
```
