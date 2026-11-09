---
title: "VSETATTR"
description: "Sets an element's JSON attributes; an empty string removes them."
version: "1.2"
command: "VSETATTR"
syntax: "VSETATTR key element json"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "vector", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
VSETATTR key element json
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
Sets the attributes of an element of the vector set at `key`, replacing any it had. An empty string removes them. Attributes are a JSON object, such as `{"color":"red","year":2024}`: [`VSIM ... FILTER`](vsim.md) selects elements by them, and `VSIM ... WITHATTRIBS` and [`VGETATTR`](vgetattr.md) return them.

KiviDB stores the string as it is given, and does not check that it is JSON. An element whose attributes are not a JSON object does not pass any `FILTER`. To set attributes when adding an element, use `SETATTR` on [`VADD`](vadd.md).

## Reply

- `OK`.
- `ERR no such element` if the element is not in the set.
- `ERR no such key` if the key does not exist.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VSETATTR points a '{"color":"blue"}'
OK
> VSIM points VALUES 3 1 0 0 FILTER '.color == "blue"'
1) "a"
> VSETATTR points a ""
OK
> VGETATTR points a
(nil)
> VSETATTR points nope '{"a":1}'
(error) ERR no such element
```
