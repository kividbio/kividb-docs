---
title: "JSON.OBJLEN"
description: "Returns the number of members of each object path matches."
version: "1.2"
command: "JSON.OBJLEN"
syntax: "JSON.OBJLEN key [path]"
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
JSON.OBJLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the number of members in each object `path` matches in the JSON document at `key`. With no path it reads the root. Only an object's own members count; the members of objects nested inside it do not.

A JSONPath reports on every value it matches; a legacy path, or no path, on the first match only. See [JSON paths](../reference/json-paths.md). A match that is not an object gives `nil` for both kinds of path. For the member names themselves, use [`JSON.OBJKEYS`](json.objkeys.md); for arrays and strings, [`JSON.ARRLEN`](json.arrlen.md) and [`JSON.STRLEN`](json.strlen.md).

## Reply

- A JSONPath: an array with one count per match, `nil` where a match is not an object; an empty array when nothing matches.
- A legacy path or no path: the count, as an integer; `nil` when the match is not an object or nothing matches.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"name":"Ada","addr":{"city":"London","zip":"N1"},"e":{}}'
OK
> JSON.OBJLEN d
(integer) 3
> JSON.OBJLEN d $.addr
1) (integer) 2
> JSON.OBJLEN d '$.*'
1) (nil)
2) (integer) 2
3) (integer) 0
> JSON.OBJLEN d .name
(nil)
```
