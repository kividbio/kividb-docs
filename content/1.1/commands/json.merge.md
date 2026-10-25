---
title: "JSON.MERGE"
description: "RFC 7396 merge patch at each match — members are merged, a null deletes, anything else replaces"
version: "1.1"
command: "JSON.MERGE"
syntax: "JSON.MERGE key path value"
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
JSON.MERGE key path value
```

**Available since:** 1.1.0 · **ACL categories:** `@json`, `@slow`, `@write`
<!-- generated: end -->
## Description

RFC 7396 merge patch at each match — members are merged, a null deletes, anything else replaces
