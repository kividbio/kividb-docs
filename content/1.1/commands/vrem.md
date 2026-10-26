---
title: "VREM"
description: "Removes elements from the vector set at key."
version: "1.1"
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
Removes elements from the vector set at `key`.

## Reply

- The number of elements removed.

## Examples

```
> VREM points b nope
(integer) 1
```
