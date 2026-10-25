---
title: "JSON.TOGGLE"
description: "Flip each matched boolean; returns the new values as 1 and 0 (a legacy path: \"true\" or \"false\")"
version: "1.1"
command: "JSON.TOGGLE"
syntax: "JSON.TOGGLE key path"
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
JSON.TOGGLE key path
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Flip each matched boolean; returns the new values as 1 and 0 (a legacy path: `"true"` or `"false"`)
