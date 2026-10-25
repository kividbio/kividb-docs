---
title: "READONLY"
description: "Per-connection flag: read commands for slots this node replicates are served here instead of redirected to the master."
version: "1.1"
command: "READONLY"
syntax: "READONLY"
group: "cluster"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["cluster", "fast"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
READONLY
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@fast`
<!-- generated: end -->
## Description

Per-connection flag: read commands for slots this node replicates are served here instead of redirected to the master.
