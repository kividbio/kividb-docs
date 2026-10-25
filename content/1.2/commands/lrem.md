---
title: "LREM"
description: "Remove occurrences of element; count > 0 from head, < 0 from tail, 0 = all"
version: "1.2"
command: "LREM"
syntax: "LREM key count element"
group: "list"
since: "1.1.0"
arity: 4
flags: ["write"]
acl_categories: ["list", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LREM key count element
```

**Available since:** 1.1.0 · **ACL categories:** `@list`, `@slow`, `@write`
<!-- generated: end -->
## Description

Remove occurrences of element; count > 0 from head, < 0 from tail, 0 = all
