---
title: "VREM"
description: "Removes elements, with their vectors and attributes, from the vector set at key, and returns how many it removed."
version: "1.2"
command: "VREM"
syntax: "VREM key element [element ...]"
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
VREM key element [element ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
Removes elements, with their vectors and attributes, from the vector set at `key`, and returns how many it removed. It takes one element or several. Elements that are not in the set are skipped, and a key that does not exist is an empty set. When the last element goes, the key is deleted.

To delete the whole set, use [`DEL`](del.md) or [`UNLINK`](unlink.md). To change an element's vector, [`VADD`](vadd.md) it again, with `SETATTR` if it should keep its attributes: without it they are removed. To change only its attributes, use [`VSETATTR`](vsetattr.md).

## Reply

- The number of elements removed, as an integer.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> VADD points VALUES 3 1 0 0 a
(integer) 1
> VADD points VALUES 3 0.9 0.1 0 b
(integer) 1
> VADD points VALUES 3 0 1 0 c
(integer) 1
> VREM points b nope
(integer) 1
> VREM points a c
(integer) 2
> EXISTS points
(integer) 0
```
