---
title: "JSON.ARRAPPEND"
description: "Appends one or more values to the end of each array path matches in the JSON document at key."
version: "1.2"
command: "JSON.ARRAPPEND"
syntax: "JSON.ARRAPPEND key path value [value ...]"
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
JSON.ARRAPPEND key path value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Appends one or more values to the end of each array `path` matches in the JSON document at `key`. Use it to grow a list inside a document, such as tags or events, without reading and rewriting the whole document.

Each `value` is JSON text: a string needs its quotes (`'"art"'`), while numbers, `true`, `null`, arrays and objects are written as they are. The values are added in the order given. Every value is parsed before the document is touched, so one that is not valid JSON fails the command and changes nothing.

A JSONPath such as `$.tags` or `$..tags` appends to every array it matches; a legacy path such as `.tags` appends to the first match only. See [JSON paths](../reference/json-paths.md). To add elsewhere than the end, use [`JSON.ARRINSERT`](json.arrinsert.md); to remove elements, [`JSON.ARRPOP`](json.arrpop.md) or [`JSON.ARRTRIM`](json.arrtrim.md).

## Reply

- A JSONPath: an array with the new length of each matched array, `nil` where a match is not an array; an empty array when nothing matches.
- A legacy path: the new length, as an integer; `nil` when the path matches nothing.
- `nil` if the key does not exist.

## Errors

- `ERR path is not an array`: a legacy path matched a value that is not an array.
- `ERR invalid JSON value`: a value is not JSON text, for example `art` without quotes.
- `ERR the path must select values, not compute one`: the path is a projection, such as `$.tags.length()`.

## Examples

```
> JSON.SET d $ '{"tags":["math","code"],"name":"Ada","n":{"tags":[1]}}'
OK
> JSON.ARRAPPEND d $.tags '"art"' '"chess"'
1) (integer) 4
> JSON.ARRAPPEND d $..tags 0
1) (integer) 5
2) (integer) 2
> JSON.ARRAPPEND d .tags '"x"'
(integer) 6
> JSON.ARRAPPEND d $.name '"x"'
1) (nil)
> JSON.ARRAPPEND d .name '"x"'
(error) ERR path is not an array
> JSON.ARRAPPEND d $.tags art
(error) ERR invalid JSON value
```
