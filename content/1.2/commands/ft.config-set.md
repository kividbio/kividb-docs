---
title: "FT.CONFIG SET"
description: "Sets a setting."
version: "1.2"
command: "FT.CONFIG SET"
syntax: "FT.CONFIG SET option value"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG SET option value
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets a setting. An unknown name, or a value of the wrong kind, is an error.

Two are acted on: `CURSOR_MAX_IDLE`, the longest a cursor may sit unread, and `MAXSEARCHRESULTS`, the largest `LIMIT` an `FT.SEARCH` may ask for. The others are kept and reported. `TIMEOUT` and `ON_TIMEOUT` do not cut a query short.

## Examples

```
> FT.CONFIG SET MAXSEARCHRESULTS 1000
OK
> FT.CONFIG SET NOPE 1
(error) Invalid option
```
