---
title: "PSETEX"
description: "Sets key to value and makes it expire after milliseconds."
version: "1.2"
command: "PSETEX"
syntax: "PSETEX key milliseconds value"
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
PSETEX key milliseconds value
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Sets `key` to `value` and makes it expire after `milliseconds`. It is `SET key value PX milliseconds`.

## Reply

- `OK`.
- `ERR invalid expire time in PSETEX` if `milliseconds` is zero or negative.

## Examples

```
> PSETEX p 1500 v
OK
> PTTL p
(integer) 1500
```
