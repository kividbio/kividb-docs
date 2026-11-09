---
title: "JSON.OBJKEYS"
description: "Returns the member names of each object path matches in the JSON document at key."
version: "1.2"
command: "JSON.OBJKEYS"
syntax: "JSON.OBJKEYS key [path]"
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
JSON.OBJKEYS key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the member names of each object `path` matches in the JSON document at `key`. With no path it reads the root. Names come in the order the members were added: changing a member's value keeps its place, while a member deleted and set again moves to the end.

A JSONPath reports on every value it matches, so the reply nests one list of names per match; a legacy path, or no path, gives the names of the first match as a flat list. See [JSON paths](../reference/json-paths.md). For the number of members only, use [`JSON.OBJLEN`](json.objlen.md). The names alone can also be read with the `~` path operator, as in `JSON.GET d '$~'`.

## Reply

- A JSONPath: an array with one array of names per match, `nil` where a match is not an object; an empty array when nothing matches.
- A legacy path or no path: an array of names; `nil` when the match is not an object or nothing matches.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36,"addr":{"city":"London","zip":"N1"}}'
OK
> JSON.OBJKEYS d
1) "name"
2) "age"
3) "addr"
> JSON.OBJKEYS d $.addr
1) 1) "city"
   2) "zip"
> JSON.OBJKEYS d '$.*'
1) (nil)
2) (nil)
3) 1) "city"
   2) "zip"
> JSON.DEL d $.name
(integer) 1
> JSON.SET d $.name '"Ada"'
OK
> JSON.OBJKEYS d
1) "age"
2) "addr"
3) "name"
```
