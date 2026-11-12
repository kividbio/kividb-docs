---
title: "JSON.ARRINDEX"
description: "Returns the index of the first element equal to value, JSON text, in each array path matches, from start to stop."
version: "1.2"
command: "JSON.ARRINDEX"
syntax: "JSON.ARRINDEX key path value [start [stop]]"
group: "json"
since: "1.1.0"
arity: -4
flags: ["readonly"]
acl_categories: ["json", "read", "slow"]
history: [{"release": "1.2.1", "change": "arity: -2 -> -4"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.ARRINDEX key path value [start [stop]]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`

**History:**

- 1.2.1: arity: -2 -> -4
<!-- generated: end -->
Returns the index of the first element equal to `value`, JSON text, in each array `path` matches, from `start` to `stop`. `stop` is excluded, and `0` means the end.

A JSONPath reports on every array it matches, `nil` for a match that is not an array. A legacy path that matches nothing, and a key that does not exist, are `ERR Path does not exist`, and a legacy path that matches a value that is not an array `WRONGTYPE wrong type of path value - expected array`, as in RedisJSON, since 1.2.1. 1.2.0 answered `nil` for a missing key or path, and `ERR path is not an array`.

## Reply

- The indexes; `-1` where there is no such element.
- `ERR Path does not exist`.
- `WRONGTYPE wrong type of path value - expected array`, for a legacy path.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRINDEX d $.tags '"code"'
1) (integer) 1
> JSON.ARRINDEX d $.tags '"none"'
1) (integer) -1
> JSON.ARRINDEX nokey $.tags '"code"'
(error) ERR Path does not exist
```
