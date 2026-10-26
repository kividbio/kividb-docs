---
title: "JSON.RESP"
description: "Returns each value path matches in RESP rather than JSON text: null as nil, booleans as true and false, integers as integers, other numbers and strings as bulk strings, an array as [ followed by its…"
version: "1.2"
command: "JSON.RESP"
syntax: "JSON.RESP key [path]"
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
JSON.RESP key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns each value `path` matches in RESP rather than JSON text: `null` as `nil`, booleans as `true` and `false`, integers as integers, other numbers and strings as bulk strings, an array as `[` followed by its elements, an object as `{` followed by its names and values.

## Examples

```
> JSON.SET d $ '{"name":"Ada","tags":[],"active":true}'
OK
> JSON.RESP d
1) {
2) "name"
3) "Ada"
4) "tags"
5) 1) [
6) "active"
7) true
```
