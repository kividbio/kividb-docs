---
title: "JSON.ARRINSERT"
description: "Inserts values, each JSON text, before index in each array path matches."
version: "1.1"
command: "JSON.ARRINSERT"
syntax: "JSON.ARRINSERT key path index value [value ...]"
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
JSON.ARRINSERT key path index value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Inserts values, each JSON text, before `index` in each array `path` matches. Negative indexes count from the end.

## Reply

- The new lengths.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRINSERT d $.tags 0 '"first"'
1) (integer) 3
```
