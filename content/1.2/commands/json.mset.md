---
title: "JSON.MSET"
description: "JSON.SET for several key-path-value triples; every argument is checked before any key is touched"
version: "1.2"
command: "JSON.MSET"
syntax: "JSON.MSET key path value [key path value ...]"
group: "json"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["json", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
JSON.MSET key path value [key path value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

`JSON.SET` for several key-path-value triples; every argument is checked before any key is touched
