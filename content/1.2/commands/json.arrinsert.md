---
title: "JSON.ARRINSERT"
description: "Inserts one or more values into each array path matches, before the element at index."
version: "1.2"
command: "JSON.ARRINSERT"
syntax: "JSON.ARRINSERT key path index value [value ...]"
group: "json"
since: "1.1.0"
arity: -5
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: [{"release": "1.2.1", "change": "arity: -2 -> -5"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.ARRINSERT key path index value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`

**History:**

- 1.2.1: arity: -2 -> -5
<!-- generated: end -->
Inserts one or more values into each array `path` matches, before the element at `index`. The values go in together, in the order given, and the elements from `index` on move up to make room.

- `index` `0` inserts at the front. The array's length inserts at the end, as [`JSON.ARRAPPEND`](json.arrappend.md) does.
- A negative `index` counts from the end: `-1` inserts before the last element.
- An `index` outside `-length` to `length` is out of bounds. That array is left alone: a JSONPath reports `nil` for it, and a legacy path fails with an error.

Each `value` is JSON text, so a string needs its quotes (`'"first"'`). A JSONPath inserts into every array it matches; a legacy path into the first match only. See [JSON paths](../reference/json-paths.md).

## Reply

- A JSONPath: an array with the new length of each matched array, `nil` where a match is not an array or `index` is out of bounds for it; an empty array when nothing matches.
- A legacy path: the new length, as an integer; `nil` when the path matches nothing.
- `nil` if the key does not exist.

## Errors

- `ERR index out of bounds` and `ERR path is not an array`, for a legacy path.
- `ERR index must be an integer`.
- `ERR invalid JSON value`: a value is not JSON text.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"]}'
OK
> JSON.ARRINSERT d $.tags 0 '"first"'
1) (integer) 3
> JSON.ARRINSERT d $.tags -1 '"beforelast"'
1) (integer) 4
> JSON.ARRINSERT d $.tags 4 '"end"'
1) (integer) 5
> JSON.GET d .tags
"[\"first\",\"math\",\"beforelast\",\"code\",\"end\"]"
> JSON.ARRINSERT d $.tags 6 '"x"'
1) (nil)
> JSON.ARRINSERT d .tags 6 '"x"'
(error) ERR index out of bounds
> JSON.ARRINSERT d .tags 1 '"a"' '"b"'
(integer) 7
```
