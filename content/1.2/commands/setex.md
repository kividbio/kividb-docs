---
title: "SETEX"
description: "Sets key to value and makes it expire after seconds."
version: "1.2"
command: "SETEX"
syntax: "SETEX key seconds value"
group: "string"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["slow", "string", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SETEX key seconds value
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Sets `key` to `value` and makes it expire after `seconds`. It is `SET key value EX seconds`.

## Reply

- `OK`.
- `ERR invalid expire time in SETEX` if `seconds` is zero or negative.

## Examples

```
> SETEX session 100 data
OK
> TTL session
(integer) 100
```
