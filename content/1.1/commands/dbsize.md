---
title: "DBSIZE"
description: "Returns the number of keys in the current database."
version: "1.1"
command: "DBSIZE"
syntax: "DBSIZE"
group: "server"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "server"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DBSIZE
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@server`
<!-- generated: end -->
Returns the number of keys in the current database.

## Examples

```
> DBSIZE
(integer) 0
```
