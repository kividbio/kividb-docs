---
title: "JSON.SET"
description: "Sets the value at path in the JSON document at key to value, which is JSON text."
version: "1.2"
command: "JSON.SET"
syntax: "JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]"
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
JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Sets the value at `path` in the JSON document at `key` to `value`, which is JSON text. A JSONPath sets every value it matches. If the path matches nothing but ends in a member name under one existing object, that member is added. A new key must be created at the root, `$`.

See [JSON paths](../reference/json-paths.md) for how paths work.

## Options

| Option | Effect |
|---|---|
| `NX` | Set only if the path matches nothing. |
| `XX` | Set only if the path matches something. |
| `FPHA FP16 \| BF16 \| FP32 \| FP64` | The floating-point type arrays of floats in `value` are stored as (Redis 8.8). |

## Reply

- `OK`.
- `nil` if `NX` or `XX` was not met, or nothing was set.
- `ERR new objects must be created at the root` for a new key and a path other than `$`.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36}'
OK
> JSON.SET d $.age 37
OK
> JSON.SET d $.email '"ada@x"'
OK
> JSON.SET d $.age 1 NX
(nil)
> JSON.SET new $.a 1
(error) ERR new objects must be created at the root
```
