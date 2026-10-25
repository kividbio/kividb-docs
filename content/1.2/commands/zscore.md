---
title: "ZSCORE"
description: "Return the score of a member, or nil"
version: "1.2"
command: "ZSCORE"
syntax: "ZSCORE key member"
group: "sorted-set"
since: "1.1.0"
arity: 3
flags: ["fast", "readonly"]
acl_categories: ["fast", "read", "sortedset"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ZSCORE key member
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@read`, `@sortedset`
<!-- generated: end -->
## Description

Return the score of a member, or nil
