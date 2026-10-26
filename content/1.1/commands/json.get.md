---
title: "JSON.GET"
description: "Returns values from the JSON document at key, as JSON text."
version: "1.1"
command: "JSON.GET"
syntax: "JSON.GET key [INDENT indent] [NEWLINE newline] [SPACE space] [path ...]"
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
JSON.GET key [INDENT indent] [NEWLINE newline] [SPACE space] [path ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns values from the JSON document at `key`, as JSON text.

- No path: the whole document.
- One path: a JSONPath gives a JSON array of its matches; a legacy path gives the first match.
- Several paths: a JSON object with one member per path.

`INDENT`, `NEWLINE` and `SPACE` set the strings used to lay out the text.

## Reply

- JSON text, as a bulk string.
- `nil` if the key does not exist.

## Examples

```
> JSON.SET d $ '{"name":"Ada","age":36,"addr":{"city":"London"}}'
OK
> JSON.GET d $.name
"[\"Ada\"]"
> JSON.GET d .name
"\"Ada\""
> JSON.GET d $.name $.age
"{\"$.name\":[\"Ada\"],\"$.age\":[36]}"
> JSON.GET d $..city
"[\"London\"]"
```
