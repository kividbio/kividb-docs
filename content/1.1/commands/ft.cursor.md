---
title: "FT.CURSOR"
description: "Reads and closes the cursors FT.AGGREGATE ..."
version: "1.1"
command: "FT.CURSOR"
syntax: "FT.CURSOR"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
subcommands: ["FT.CURSOR DEL", "FT.CURSOR READ"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CURSOR
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`

Subcommands: [FT.CURSOR DEL](ft.cursor-del.md), [FT.CURSOR READ](ft.cursor-read.md)
<!-- generated: end -->
Reads and closes the cursors [`FT.AGGREGATE ... WITHCURSOR`](ft.aggregate.md) returns. See its subcommands.
