---
title: "JSON.TOGGLE"
description: "Flips each boolean path matches."
version: "1.2"
command: "JSON.TOGGLE"
syntax: "JSON.TOGGLE key path"
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
JSON.TOGGLE key path
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Flips each boolean `path` matches.

## Reply

- A JSONPath: the new values as `1` and `0`. A legacy path: `"true"` or `"false"`.

## Examples

```
> JSON.SET d $ '{"active":true}'
OK
> JSON.TOGGLE d $.active
1) (integer) 0
> JSON.TOGGLE d .active
"true"
```
