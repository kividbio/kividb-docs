---
title: "JSON.MSET"
description: "JSON.SET for several key-path-value triples at once."
version: "1.1"
command: "JSON.MSET"
syntax: "JSON.MSET key path value [key path value ...]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.MSET key path value [key path value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
[`JSON.SET`](json.set.md) for several key-path-value triples at once. Every argument is checked before any key is changed.

## Reply

- `OK`.

## Examples

```
> JSON.MSET a $ 1 b $ 2
OK
```
