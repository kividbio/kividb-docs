---
title: "MSET"
description: "Sets several keys to string values in one step."
version: "1.1"
command: "MSET"
syntax: "MSET key value [key value ...]"
group: "string"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MSET key value [key value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Sets several keys to string values in one step. Existing values are replaced, and their expiries removed.

## Reply

- `OK`; `MSET` does not fail for a key's existing value or type.
- A wrong-number-of-arguments error if the keys and values do not pair up.

## Examples

```
> MSET a 1 b 2
OK
> MGET a b
1) "1"
2) "2"
```
