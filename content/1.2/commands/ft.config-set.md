---
title: "FT.CONFIG SET"
description: "Set one; an unknown option or a value of the wrong kind is an error."
version: "1.2"
command: "FT.CONFIG SET"
syntax: "FT.CONFIG SET option value"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG SET option value
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Set one; an unknown option or a value of the wrong kind is an error. Acted on: `CURSOR_MAX_IDLE` (the longest a cursor may sit unread) and `MAXSEARCHRESULTS` (the largest `LIMIT` an `FT.SEARCH` may ask for). The rest are kept and reported — `TIMEOUT` and `ON_TIMEOUT` in particular do not cut a query short
