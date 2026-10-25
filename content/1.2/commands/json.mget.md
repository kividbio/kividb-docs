---
title: "JSON.MGET"
description: "Evaluates path in the JSON documents at several keys."
version: "1.2"
command: "JSON.MGET"
syntax: "JSON.MGET key [key ...] path"
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
JSON.MGET key [key ...] path
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@read`, `@slow`
<!-- generated: end -->
Evaluates `path` in the JSON documents at several keys.

## Reply

- An array with one element per key: the JSON text the path gives, or `nil` for a key that does not exist or is not a JSON document.

## Examples

```
> JSON.MSET a $ 1 b $ 2
OK
> JSON.MGET a b missing $
1) "[1]"
2) "[2]"
3) (nil)
```
