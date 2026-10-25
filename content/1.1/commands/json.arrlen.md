---
title: "JSON.ARRLEN"
description: "Returns the length of each array path matches."
version: "1.1"
command: "JSON.ARRLEN"
syntax: "JSON.ARRLEN key [path]"
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
JSON.ARRLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the length of each array `path` matches.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRLEN d $.tags
1) (integer) 2
```
