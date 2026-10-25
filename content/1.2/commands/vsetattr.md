---
title: "VSETATTR"
description: "Attach a JSON attributes string to an element; pass empty string \"\" to remove; AOF-logged"
version: "1.2"
command: "VSETATTR"
syntax: "VSETATTR key element json"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "vector", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VSETATTR key element json
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
## Description

Attach a JSON attributes string to an element; pass empty string `""` to remove; AOF-logged
