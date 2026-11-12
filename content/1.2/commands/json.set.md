---
title: "JSON.SET"
description: "Sets the value at path in the JSON document at key to value, which is JSON text."
version: "1.2"
command: "JSON.SET"
syntax: "JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]"
group: "json"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: [{"release": "1.2.1", "change": "arity: -2 -> -4"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.SET key path value [NX | XX] [FPHA FP16 | BF16 | FP32 | FP64]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`

**History:**

- 1.2.1: arity: -2 -> -4
<!-- generated: end -->
Sets the value at `path` in the JSON document at `key` to `value`, which is JSON text. A JSONPath sets every value it matches. If the path matches nothing but ends in a member name under one existing object, that member is added. A new key must be created at the root, `$`. A document is at most 128 levels deep: a write that would nest one deeper is refused with `ERR recursion limit exceeded`, as in RedisJSON, since 1.2.1 ([GHSA-qh83-449g-hwm5](https://github.com/kividbio/kividb/security/advisories/GHSA-qh83-449g-hwm5)). Numbers keep every digit: a double that needs 17 significant digits, such as `13.326500000000001`, comes back as it was sent, where 1.2.0 could return the double next to it.

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
- `ERR recursion limit exceeded` for a write that would nest the document 128 levels or deeper.

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
