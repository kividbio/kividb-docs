---
title: "GETDEL"
description: "Returns the string at key and deletes the key, in one step."
version: "1.2"
command: "GETDEL"
syntax: "GETDEL key"
group: "string"
since: "1.1.0"
arity: 2
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GETDEL key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Returns the string at `key` and deletes the key, in one step.

## Reply

- The value, or `nil` if the key did not exist.
- A `WRONGTYPE` error, and nothing deleted, if the key is not a string.

## Examples

```
> SET a v
OK
> GETDEL a
"v"
> GET a
(nil)
```
