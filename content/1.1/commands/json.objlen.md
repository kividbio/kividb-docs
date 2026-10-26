---
title: "JSON.OBJLEN"
description: "Returns the number of members of each object path matches."
version: "1.1"
command: "JSON.OBJLEN"
syntax: "JSON.OBJLEN key [path]"
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
JSON.OBJLEN key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Returns the number of members of each object `path` matches.

## Examples

```
> JSON.SET d $ '{"name":"Ada","addr":{"city":"London"}}'
OK
> JSON.OBJLEN d
(integer) 2
> JSON.OBJLEN d $.addr
1) (integer) 1
```
