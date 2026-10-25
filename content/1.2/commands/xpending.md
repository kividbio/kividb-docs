---
title: "XPENDING"
description: "Return pending entry summary or detail list"
version: "1.2"
command: "XPENDING"
syntax: "XPENDING key group [[IDLE ms] start end count [consumer]]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["readonly"]
acl_categories: ["read", "slow", "stream"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XPENDING key group [[IDLE ms] start end count [consumer]]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@stream`
<!-- generated: end -->
## Description

Return pending entry summary or detail list
