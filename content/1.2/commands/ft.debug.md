---
title: "FT.DEBUG"
description: "Maintenance of search indexes."
version: "1.2"
command: "FT.DEBUG"
syntax: "FT.DEBUG"
group: "vector-search"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["read", "search", "slow"]
history: []
subcommands: ["FT.DEBUG COMPACT"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.DEBUG
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@search`, `@slow`

Subcommands: [FT.DEBUG COMPACT](ft.debug-compact.md)
<!-- generated: end -->
Maintenance of search indexes. See its subcommand, [`FT.DEBUG COMPACT`](ft.debug-compact.md).

Two more turn parts of an index's machinery off and on again, to compare; they are for diagnosis:

- `FT.DEBUG POSTINGS <index> ON|OFF`: with `OFF`, TAG and NUMERIC clauses are tried on every document, as before 1.2, rather than read from the index's postings.
- `FT.DEBUG PAGE <index> ON|OFF`: with `OFF`, a TAG or NUMERIC query reads every match, rather than only those of the page it returns.

```
> FT.DEBUG POSTINGS products OFF
OK
> FT.DEBUG POSTINGS products ON
OK
```
