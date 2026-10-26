---
title: "JSON.STRAPPEND"
description: "Appends a JSON string to each string path matches."
version: "1.1"
command: "JSON.STRAPPEND"
syntax: "JSON.STRAPPEND key [path] value"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.STRAPPEND key [path] value
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Appends a JSON string to each string `path` matches. `value` is JSON text, so it is quoted: `'" L."'`.

## Reply

- A JSONPath: the new lengths, `nil` where a match is not a string. A legacy path: the one new length.

## Examples

```
> JSON.SET d $ '{"name":"Ada"}'
OK
> JSON.STRAPPEND d $.name '" L."'
1) (integer) 6
```
