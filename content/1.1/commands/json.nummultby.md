---
title: "JSON.NUMMULTBY"
description: "Multiplies each number path matches by number, with the same replies as JSON.NUMINCRBY."
version: "1.1"
command: "JSON.NUMMULTBY"
syntax: "JSON.NUMMULTBY key path number"
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
JSON.NUMMULTBY key path number
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Multiplies each number `path` matches by `number`, with the same replies as [`JSON.NUMINCRBY`](json.numincrby.md).

## Examples

```
> JSON.SET d $ '{"age":40}'
OK
> JSON.NUMMULTBY d $.age 2
"[80]"
```
