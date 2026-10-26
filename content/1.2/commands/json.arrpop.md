---
title: "JSON.ARRPOP"
description: "Removes and returns an element from each array path matches: the last one, or the one at index."
version: "1.2"
command: "JSON.ARRPOP"
syntax: "JSON.ARRPOP key [path [index]]"
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
JSON.ARRPOP key [path [index]]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Removes and returns an element from each array `path` matches: the last one, or the one at `index`. An index out of range takes the nearest end.

## Reply

- The elements removed, as JSON text.

## Examples

```
> JSON.SET d $ '{"tags":["first","math","code"]}'
OK
> JSON.ARRPOP d $.tags
1) "\"code\""
> JSON.ARRPOP d $.tags 0
1) "\"first\""
```
