---
title: "TIME"
description: "Returns the server's clock: Unix seconds, and the microseconds within that second, as two bulk strings."
version: "1.2"
command: "TIME"
syntax: "TIME"
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
TIME
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@server`
<!-- generated: end -->
Returns the server's clock: Unix seconds, and the microseconds within that second, as two bulk strings.

## Examples

```
> TIME
1) "1792968400"
2) "89815"
```
