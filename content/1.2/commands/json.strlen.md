---
title: "JSON.STRLEN"
description: "Returns the length of each string path matches; nil for a match that is not a string."
version: "1.2"
command: "JSON.STRLEN"
syntax: "JSON.STRLEN key [path]"
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
JSON.STRLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the length of each string `path` matches; `nil` for a match that is not a string.

## Examples

```
> JSON.SET d $ '{"name":"Ada L."}'
OK
> JSON.STRLEN d $.name
1) (integer) 6
```
