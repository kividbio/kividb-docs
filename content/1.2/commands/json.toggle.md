---
title: "JSON.TOGGLE"
description: "Flips each boolean path matches."
version: "1.2"
command: "JSON.TOGGLE"
syntax: "JSON.TOGGLE key path"
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
JSON.TOGGLE key path
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Flips each boolean `path` matches in the JSON document at `key`: `true` becomes `false` and `false` becomes `true`. Use it for flags such as `active` or `muted` without reading the value first. The path is required; to toggle a document that is a single boolean, give `$`.

A JSONPath flips every boolean it matches and leaves other values alone; a legacy path flips the first match only. See [JSON paths](../reference/json-paths.md).

## Reply

- A JSONPath: an array with each new value as `1` (true) or `0` (false), `nil` where a match is not a boolean; an empty array when nothing matches.
- A legacy path: the new value as the bulk string `"true"` or `"false"`; `nil` when the path matches nothing.
- `nil` if the key does not exist.

## Errors

- `ERR path is not a boolean`, for a legacy path.

## Examples

```
> JSON.SET t $ '{"active":true,"x":1,"n":{"active":false}}'
OK
> JSON.TOGGLE t $.active
1) (integer) 0
> JSON.TOGGLE t .active
"true"
> JSON.TOGGLE t $..active
1) (integer) 0
2) (integer) 1
> JSON.TOGGLE t $.x
1) (nil)
> JSON.TOGGLE t .x
(error) ERR path is not a boolean
> JSON.GET t
"{\"active\":false,\"x\":1,\"n\":{\"active\":true}}"
```
