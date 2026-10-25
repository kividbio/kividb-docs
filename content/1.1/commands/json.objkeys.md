---
title: "JSON.OBJKEYS"
description: "Returns the member names of each object path matches, in the order they were added."
version: "1.1"
command: "JSON.OBJKEYS"
syntax: "JSON.OBJKEYS key [path]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.OBJKEYS key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the member names of each object `path` matches, in the order they were added.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36}'
OK
> JSON.OBJKEYS d
1) "name"
2) "age"
```
