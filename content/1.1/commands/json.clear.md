---
title: "JSON.CLEAR"
description: "Empty each matched array and object and set each matched number to 0; returns how many values changed"
version: "1.1"
command: "JSON.CLEAR"
syntax: "JSON.CLEAR key [path]"
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
JSON.CLEAR key [path]
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

Empty each matched array and object and set each matched number to 0; returns how many values changed
