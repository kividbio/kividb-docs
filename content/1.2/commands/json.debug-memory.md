---
title: "JSON.DEBUG MEMORY"
description: "Returns the approximate size, in bytes, of each value path matches in the JSON document at key; of the whole document with no path."
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

The size KiviDB reports is the length of the value written as compact JSON text, the form [`JSON.GET`](json.get.md) returns without formatting options. It is not measured from the server's allocations, which are larger: for the memory a key takes, use [`MEMORY USAGE`](memory-usage.md). A string's size includes its two quotes.

A JSONPath reports on every value it matches; a legacy path on the first match only. See [JSON paths](../reference/json-paths.md).

## Reply

- A JSONPath: an array with one size per match; an empty array when nothing matches.
- A legacy path or no path: the size, as an integer; `nil` when the path matches nothing.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"name":"Ada","tags":["math","code"],"addr":{"city":"London"}}'
OK
> JSON.DEBUG MEMORY d
(integer) 62
> JSON.DEBUG MEMORY d $.name
1) (integer) 5
> JSON.DEBUG MEMORY d .tags
(integer) 15
> JSON.DEBUG MEMORY d '$.*'
1) (integer) 5
2) (integer) 15
3) (integer) 17
> MEMORY USAGE d
(integer) 190
```
