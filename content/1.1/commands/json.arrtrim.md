---
title: "JSON.ARRTRIM"
description: "Keeps only the elements from start to stop, both included, in each array path matches."
version: "1.1"
command: "JSON.ARRTRIM"
syntax: "JSON.ARRTRIM key path start stop"
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
JSON.ARRTRIM key path start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Keeps only the elements from `start` to `stop`, both included, in each array `path` matches.

## Reply

- The new lengths.

## Examples

```
> JSON.SET d $ '{"tags":["a","b","c","d"]}'
OK
> JSON.ARRTRIM d $.tags 0 1
1) (integer) 2
> JSON.GET d $.tags
"[[\"a\",\"b\"]]"
```
