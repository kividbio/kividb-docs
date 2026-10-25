---
title: "JSON.ARRAPPEND"
description: "Appends values, each JSON text, to each array path matches."
version: "1.1"
command: "JSON.ARRAPPEND"
syntax: "JSON.ARRAPPEND key path value [value ...]"
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
JSON.ARRAPPEND key path value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Appends values, each JSON text, to each array `path` matches.

## Reply

- The new lengths; `nil` where a match is not an array.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRAPPEND d $.tags '"art"' '"chess"'
1) (integer) 4
```
