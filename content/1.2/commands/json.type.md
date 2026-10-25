---
title: "JSON.TYPE"
description: "Returns the type of each value path matches: object, array, string, integer, number, boolean or null."
version: "1.2"
command: "JSON.TYPE"
syntax: "JSON.TYPE key [path]"
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
JSON.TYPE key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the type of each value `path` matches: `object`, `array`, `string`, `integer`, `number`, `boolean` or `null`.

## Reply

- A JSONPath: an array of types. A legacy path, or none: one type.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36,"tags":[],"addr":{},"active":true}'
OK
> JSON.TYPE d
"object"
> JSON.TYPE d $.*
1) "string"
2) "integer"
3) "array"
4) "object"
5) "boolean"
```
