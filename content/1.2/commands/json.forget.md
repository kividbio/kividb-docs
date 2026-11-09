---
title: "JSON.FORGET"
description: "Another name for JSON.DEL."
version: "1.2"
command: "JSON.FORGET"
syntax: "JSON.FORGET key [path]"
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
JSON.FORGET key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
Another name for [`JSON.DEL`](json.del.md): it takes the same arguments and gives the same reply. It deletes the values `path` matches in the JSON document at `key`. Deleting the root, which is what happens with no path, deletes the key itself. A member removed from an object leaves the other members in their order.

A JSONPath deletes every value it matches. A legacy path that matches several values, such as `..a`, also deletes all of them. See [JSON paths](../reference/json-paths.md).

## Reply

- The number of values deleted, as an integer.
- `0` if the key does not exist or the path matches nothing.

## Errors

- `ERR the path must select values, not compute one`: the path is a projection.
- `WRONGTYPE` if the key holds a value that is not a JSON document.

## Examples

```
> JSON.SET d $ '{"name":"Ada","addr":{"city":"London","zip":"N1"}}'
OK
> JSON.FORGET d $.addr.zip
(integer) 1
> JSON.FORGET d $.nope
(integer) 0
> JSON.FORGET d
(integer) 1
> EXISTS d
(integer) 0
```
