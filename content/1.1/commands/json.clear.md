---
title: "JSON.CLEAR"
description: "Empties each array and object path matches, and sets each number it matches to 0."
version: "1.1"
command: "JSON.CLEAR"
syntax: "JSON.CLEAR key [path]"
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
JSON.CLEAR key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Empties each array and object `path` matches, and sets each number it matches to `0`.

## Reply

- The number of values changed.

## Examples

```
> JSON.SET d $ '{"tags":["a","b"]}'
OK
> JSON.CLEAR d $.tags
(integer) 1
> JSON.GET d $.tags
"[[]]"
```
