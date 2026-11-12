---
title: "JSON.NUMMULTBY"
description: "Multiplies each number path matches in the JSON document at key by number, and stores the result in place."
version: "1.2"
command: "JSON.NUMMULTBY"
syntax: "JSON.NUMMULTBY key path number"
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
JSON.NUMMULTBY key path number
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`

**History:**

- 1.2.1: arity: -2 -> 4
<!-- generated: end -->
Multiplies each number `path` matches in the JSON document at `key` by `number`, and stores the result in place. The replies are the same as those of [`JSON.NUMINCRBY`](json.numincrby.md).

`number` is a JSON number, such as `2`, `0.5` or `1e3`; anything else, a quoted `"2"` included, is refused. The product is an integer only when both numbers are integers, so `1.5` times `2` is `3.0`, as in RedisJSON. Two integers whose product does not fit a 64-bit integer fail with `ERR numeric overflow`. Every result is worked out before anything is written: an overflow, or a product that is not a finite number, fails the command and leaves the document as it was.

Before 1.2.1, a whole product was stored as an integer (`1.5` times `2` was `3`), and two integers whose product did not fit gave a float. A client that reads such a result as an integer may need to change.

A JSONPath multiplies every number it matches; a legacy path the first match only. See [JSON paths](../reference/json-paths.md).

## Reply

- A JSONPath: the new values as one JSON array in a bulk string, with `null` where a match is not a number, and `"[]"` when nothing matches. In RESP3, an array of numbers, with `nil` for those.
- A legacy path: the new value, as a bulk string; `nil` when the path matches nothing.
- `nil` if the key does not exist.

## Errors

- `ERR path is not a number`, for a legacy path.
- `ERR value must be a number`.
- `ERR numeric overflow`.
- `ERR result is not a finite number`.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":40,"p":[1.5,2,"x"]}'
OK
> JSON.NUMMULTBY d $.age 2
"[80]"
> JSON.NUMMULTBY d .age 0.5
"40.0"
> JSON.NUMMULTBY d '$.p[*]' 2
"[3.0,4,null]"
> JSON.NUMMULTBY d .name 2
(error) ERR path is not a number
> JSON.NUMMULTBY d $.age 1e308
(error) ERR result is not a finite number
```
