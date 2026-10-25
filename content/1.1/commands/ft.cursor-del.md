---
title: "FT.CURSOR DEL"
description: "Closes a cursor before it is read to the end."
version: "1.1"
command: "FT.CURSOR DEL"
syntax: "FT.CURSOR DEL index cursor_id"
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
FT.CURSOR DEL index cursor_id
```

**Available since:** 1.1.0
<!-- generated: end -->
Closes a cursor before it is read to the end.

## Reply

- `OK`.
- `Cursor does not exist`, also for one read to the end.
