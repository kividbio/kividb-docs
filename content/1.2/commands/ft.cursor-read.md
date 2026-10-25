---
title: "FT.CURSOR READ"
description: "The next rows of an FT.AGGREGATE … WITHCURSOR, and the cursor to read on with — 0 when there are no more."
version: "1.2"
command: "FT.CURSOR READ"
syntax: "FT.CURSOR READ index cursor_id [COUNT n]"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CURSOR"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.CURSOR READ index cursor_id [COUNT n]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

The next rows of an `FT.AGGREGATE … WITHCURSOR`, and the cursor to read on with — `0` when there are no more. A cursor holds the result as it was when the aggregation ran; it is dropped after `MAXIDLE` unread, and when its index is
