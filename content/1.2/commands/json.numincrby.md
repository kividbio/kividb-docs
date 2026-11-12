---
title: "JSON.NUMINCRBY"
description: "Adds number to each number path matches."
version: "1.2"
command: "JSON.NUMINCRBY"
syntax: "JSON.NUMINCRBY key path number"
group: "json"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: [{"release": "1.2.1", "change": "arity: -2 -> 4"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.NUMINCRBY key path number
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`

**History:**

- 1.2.1: arity: -2 -> 4
<!-- generated: end -->
Adds `number` to each number `path` matches. The result is an integer only when both numbers are integers, so a float stays a float even when the result is whole: `1.5` plus `1.5` is `3.0`, as in RedisJSON. Two integers whose sum does not fit a 64-bit integer fail with `ERR numeric overflow`, and a result that is not a finite number fails too; either way nothing changes, on every path.

Both are since 1.2.1. In 1.2.0, a whole result was stored as an integer (`3`, which `JSON.TYPE` then called `integer`), and an integer overflow gave a float. A client that reads such a result as an integer may need to change. An append-only file written by an earlier release replays to the new form, with the same numeric value, and an overflow it holds is refused on replay, so the value stays the integer.

## Reply

- A JSONPath: the new values, as one JSON array in a bulk string, with `null` where a match is not a number. In RESP3, an array of numbers.
- A legacy path: the one new value.

## Errors

- `ERR path is not a number`, for a legacy path.
- `ERR numeric overflow`.
- `ERR result is not a finite number`.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36}'
OK
> JSON.NUMINCRBY d $.age 2
"[38]"
> JSON.NUMINCRBY d .age 1
"39"
> JSON.NUMINCRBY d $.name 1
"[null]"
> JSON.SET f $ '{"x":1.5,"n":9223372036854775807}'
OK
> JSON.NUMINCRBY f $.x 1.5
"[3.0]"
> JSON.NUMINCRBY f $.n 1
(error) ERR numeric overflow
```
