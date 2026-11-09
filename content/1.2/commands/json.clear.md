---
title: "JSON.CLEAR"
description: "Empties each array and object path matches, and sets each number it matches to 0."
version: "1.2"
command: "JSON.CLEAR"
syntax: "JSON.CLEAR key [path]"
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
JSON.CLEAR key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Resets values in a JSON document without removing them: each array and object `path` matches is emptied, and each number becomes `0`. Strings, booleans and `null` are left as they are. With no path it clears the root, so a document that is an object becomes `{}` and the key stays. Use it to reset counters or collections while keeping the document's shape; to remove values, use [`JSON.DEL`](json.del.md).

A JSONPath clears every value it matches. A legacy path that matches several values, such as `..a`, also clears all of them. See [JSON paths](../reference/json-paths.md).

## Reply

- The number of values changed, as an integer. An array or object that was already empty, or a number that was already `0`, is not counted.
- `0` if the key does not exist or the path matches nothing.

## Errors

- `ERR the path must select values, not compute one`: the path is a projection, such as `$.length()`.

## Examples

```
> JSON.SET d $ '{"tags":["a","b"],"n":5,"f":1.5,"s":"str","b":true,"o":{"x":1}}'
OK
> JSON.CLEAR d $.tags
(integer) 1
> JSON.CLEAR d '$.*'
(integer) 3
> JSON.GET d
"{\"tags\":[],\"n\":0,\"f\":0,\"s\":\"str\",\"b\":true,\"o\":{}}"
> JSON.CLEAR d
(integer) 1
> JSON.GET d
"{}"
```
