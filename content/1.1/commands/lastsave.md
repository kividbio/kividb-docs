---
title: "LASTSAVE"
description: "Returns the Unix time of the last snapshot saved, 0 if none."
version: "1.1"
command: "LASTSAVE"
syntax: "LASTSAVE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["admin", "fast"]
acl_categories: ["admin", "dangerous", "fast", "server"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LASTSAVE
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@fast`, `@server`
<!-- generated: end -->
Returns the Unix time of the last snapshot saved, `0` if none.

## Examples

```
> LASTSAVE
(integer) 0
```
