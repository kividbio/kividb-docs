---
title: "JSON.DEBUG MEMORY"
description: "Reports the size, in bytes, of each value path matches in the JSON document at key, or of the whole document with no path."
version: "1.2"
command: "JSON.DEBUG MEMORY"
syntax: "JSON.DEBUG MEMORY key [path]"
group: "json"
since: "1.1.0"
history: []
container: "JSON.DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.DEBUG MEMORY key [path]
```

**Available since:** 1.1.0
<!-- generated: end -->
Reports the size, in bytes, of each value `path` matches in the JSON document at `key`, or of the whole document with no path. Use it to find which parts of a document are large.

The size is the bytes the value takes in the server's memory, as in RedisJSON: the value itself and what it points to, so a small value takes several times its length as text. [`MEMORY USAGE`](memory-usage.md) gives an estimate for the whole key in another way: for a JSON document, the length of its compact JSON text plus 128 bytes, and the key name's length too if it is over 24 bytes.

Before 1.2.1, `JSON.DEBUG MEMORY` reported the length of the value's compact JSON text, and `nil` for a key that did not exist.

A JSONPath reports on every value it matches; a legacy path on the first match only. See [JSON paths](../reference/json-paths.md).

## Reply

- A JSONPath: an array with one size per match; an empty array when nothing matches.
- A legacy path or no path: the size, as an integer.
- `ERR Path does not exist`, for a legacy path that matches nothing.
- For a key that does not exist, `0` with a legacy path or no path, and an empty array with a JSONPath.

## Examples

```
> JSON.SET d $ '{"name":"Ada","tags":["math","code"],"addr":{"city":"London"}}'
OK
> JSON.DEBUG MEMORY d
(integer) 701
> JSON.DEBUG MEMORY d $.name
1) (integer) 75
> JSON.DEBUG MEMORY d .tags
(integer) 224
> JSON.DEBUG MEMORY d '$.*'
1) (integer) 75
2) (integer) 224
3) (integer) 195
> MEMORY USAGE d
(integer) 190
> JSON.DEBUG MEMORY nokey
(integer) 0
```
