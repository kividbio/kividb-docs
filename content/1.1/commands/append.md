---
title: "APPEND"
description: "Appends value to the string at key."
version: "1.1"
command: "APPEND"
syntax: "APPEND key value"
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
APPEND key value
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@string`, `@write`
<!-- generated: end -->
Appends `value` to the string at `key`. A missing key is created with `value`. The key's expiry, if it has one, is kept.

## Reply

- The length of the string afterwards.
- A `WRONGTYPE` error if the key is not a string.

## Examples

```
> SET k hello
OK
> APPEND k " world"
(integer) 11
> GET k
"hello world"
```
