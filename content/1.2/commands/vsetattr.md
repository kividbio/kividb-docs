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
Sets an element's JSON attributes; an empty string removes them.

## Examples

```
> VSETATTR points a '{"color":"blue"}'
OK
> VSETATTR points a ""
OK
> VGETATTR points a
(nil)
```
