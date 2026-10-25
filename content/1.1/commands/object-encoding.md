---
title: "OBJECT ENCODING"
description: "Returns the name of the encoding Redis would use for the value at key, from the value's size and the *-max-listpack-* and set-max-intset-entries settings."
version: "1.1"
command: "OBJECT ENCODING"
syntax: "OBJECT ENCODING key"
group: "generic"
since: "1.1.0"
history: []
container: "OBJECT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
OBJECT ENCODING key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the name of the encoding Redis would use for the value at `key`, from the value's size and the `*-max-listpack-*` and `set-max-intset-entries` settings.

KiviDB stores each type one way, whatever its size. The name is there for clients and tests that look at it.

| Type | Names |
|---|---|
| string | `int`, `embstr`, `raw` |
| list | `listpack`, `quicklist` |
| set | `listpack`, `intset`, `hashtable` |
| hash | `listpack`, `hashtable` |
| sorted set | `listpack`, `skiplist` |
| stream | `stream` |

## Examples

```
> SET a 123
OK
> OBJECT ENCODING a
"int"
> SET b hello
OK
> OBJECT ENCODING b
"embstr"
```
