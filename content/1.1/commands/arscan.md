---
title: "ARSCAN"
description: "Iterate existing elements in a range, skipping empty slots."
version: "1.1"
command: "ARSCAN"
syntax: "ARSCAN key start end [LIMIT limit]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARSCAN key start end [LIMIT limit]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Iterate existing elements in a range, skipping empty slots. Returns a **flat** `[idx, val, idx, val, ...]` array; `start > end` iterates in reverse
