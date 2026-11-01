---
title: "GETSET"
description: "Sets key to value and returns the value it held before, in one step."
version: "1.2"
command: "GETSET"
syntax: "GETSET key value"
group: "string"
since: "1.1.0"
arity: 3
flags: ["fast", "write"]
acl_categories: ["fast", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GETSET key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Sets `key` to `value` and returns the value it held before, in one step. The key's expiry is removed. `SET key value GET` does the same.

## Reply

- The old value, or `nil` if the key did not exist.
- A `WRONGTYPE` error if the key holds another type; the key is left as it was.

## Examples

```
> SET a 1
OK
> GETSET a new
"1"
> GET a
"new"
```

Before 1.2, `GETSET` of a key of another type replaced it with the string and then replied `WRONGTYPE`.
