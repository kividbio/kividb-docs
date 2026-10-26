---
title: "ARDEL"
description: "Empties the slots at the given indexes."
version: "1.1"
command: "ARDEL"
syntax: "ARDEL key index [index ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARDEL key index [index ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
Empties the slots at the given indexes.

## Reply

- The number of slots that were filled.

## Examples

```
> ARDEL a 3 9 100
(integer) 2
```
