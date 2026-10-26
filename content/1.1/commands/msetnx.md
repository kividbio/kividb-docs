---
title: "MSETNX"
description: "Sets several keys to string values only if none of them exists."
version: "1.1"
command: "MSETNX"
syntax: "MSETNX key value [key value ...]"
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
MSETNX key value [key value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@string`, `@write`
<!-- generated: end -->
Sets several keys to string values only if none of them exists. Either every key is set, or none is.

## Reply

- `1` if every key was set.
- `0` if at least one key existed; then nothing is set.

## Examples

```
> MSET a 1
OK
> MSETNX a 9 c 3
(integer) 0
> MSETNX c 3 d 4
(integer) 1
```
