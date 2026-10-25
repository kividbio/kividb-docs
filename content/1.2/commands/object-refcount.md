---
title: "OBJECT REFCOUNT"
description: "Returns 1 for a key that exists: in KiviDB a value is not shared between keys."
version: "1.2"
command: "OBJECT REFCOUNT"
syntax: "OBJECT REFCOUNT key"
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
OBJECT REFCOUNT key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns `1` for a key that exists: in KiviDB a value is not shared between keys.

## Reply

- `1`.
- `nil` if the key does not exist.

## Examples

```
> SET a 123
OK
> OBJECT REFCOUNT a
(integer) 1
```
