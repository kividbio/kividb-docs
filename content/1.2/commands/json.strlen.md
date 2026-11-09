---
title: "JSON.STRLEN"
description: "Returns the length of each string path matches; nil for a match that is not a string."
version: "1.2"
command: "JSON.STRLEN"
syntax: "JSON.STRLEN key [path]"
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
JSON.STRLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the length of each string `path` matches in the JSON document at `key`. The length is in bytes of the string's UTF-8 text, without quotes, so `"Zürich"` has length 7: `ü` takes two bytes.

A JSONPath reports on every value it matches; a legacy path, or no path, on the first match only. See [JSON paths](../reference/json-paths.md). A match that is not a string gives `nil` for both kinds of path. To add to a string, use [`JSON.STRAPPEND`](json.strappend.md), which replies with the new length in the same unit.

## Reply

- A JSONPath: an array with one length per match, `nil` where a match is not a string; an empty array when nothing matches.
- A legacy path or no path: the length, as an integer; `nil` when the match is not a string or nothing matches.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"name":"Ada L.","city":"Zürich","age":36,"kids":[{"name":"Al"},{"name":"Bea"}]}'
OK
> JSON.STRLEN d $.name
1) (integer) 6
> JSON.STRLEN d .city
(integer) 7
> JSON.STRLEN d $..name
1) (integer) 6
2) (integer) 2
3) (integer) 3
> JSON.STRLEN d $.age
1) (nil)
```
