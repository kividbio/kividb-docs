---
title: "JSON.ARRINDEX"
description: "Returns the index of the first element equal to value, JSON text, in each array path matches, from start to stop."
version: "1.1"
command: "JSON.ARRINDEX"
syntax: "JSON.ARRINDEX key path value [start [stop]]"
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
JSON.ARRINDEX key path value [start [stop]]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the index of the first element equal to `value`, JSON text, in each array `path` matches, from `start` to `stop`. `stop` is excluded, and `0` means the end.

## Reply

- The indexes; `-1` where there is no such element.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRINDEX d $.tags '"code"'
1) (integer) 1
> JSON.ARRINDEX d $.tags '"none"'
1) (integer) -1
```
