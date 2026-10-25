---
title: "GET"
description: "Returns the string stored at key."
version: "1.2"
command: "GET"
syntax: "GET key"
group: "string"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GET key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@string`
<!-- generated: end -->
Returns the string stored at `key`.

## Reply

- The value, as a bulk string.
- `nil` if the key does not exist.
- A `WRONGTYPE` error if the key holds a list, hash or other non-string value.

## Examples

```
> SET greeting hello
OK
> GET greeting
"hello"
> GET missing
(nil)
```
