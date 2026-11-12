---
title: "JSON.ARRLEN"
description: "Returns the number of elements in each array path matches in the JSON document at key."
version: "1.2"
command: "JSON.ARRLEN"
syntax: "JSON.ARRLEN key [path]"
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
JSON.ARRLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the number of elements in each array `path` matches in the JSON document at `key`. With no path it reads the root, which gives a length only when the whole document is an array.

A JSONPath such as `$..tags` reports on every array it matches; a legacy path such as `.tags` on the first match only. See [JSON paths](../reference/json-paths.md). A JSONPath reports `nil` for a match that is not an array. A legacy path that matches nothing, or a value that is not an array, is an error, `ERR Path does not exist` or `ERR Path does not exist or not an array`, as in RedisJSON, since 1.2.1; 1.2.0 answered `nil` for both. To check a value's type first, use [`JSON.TYPE`](json.type.md); for the length of strings and objects, [`JSON.STRLEN`](json.strlen.md) and [`JSON.OBJLEN`](json.objlen.md).

## Reply

- A JSONPath: an array with one length per match, `nil` where a match is not an array; an empty array when nothing matches.
- A legacy path: the length, as an integer.
- `ERR Path does not exist`, or `ERR Path does not exist or not an array`, for a legacy path.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"],"name":"Ada","n":{"tags":[1,2,3]},"e":[]}'
OK
> JSON.ARRLEN d $.tags
1) (integer) 2
> JSON.ARRLEN d .tags
(integer) 2
> JSON.ARRLEN d $..tags
1) (integer) 2
2) (integer) 3
> JSON.ARRLEN d '$.*'
1) (integer) 2
2) (nil)
3) (nil)
4) (integer) 0
> JSON.ARRLEN d .name
(error) ERR Path does not exist or not an array
> JSON.ARRLEN d $.nope
(empty array)
```
