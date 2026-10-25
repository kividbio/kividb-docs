---
title: "JSON.DEL"
description: "Delete every value the path matches; returns how many."
version: "1.1"
command: "JSON.DEL"
syntax: "JSON.DEL key [path]"
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
JSON.DEL key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Delete every value the path matches; returns how many. The root deletes the key
