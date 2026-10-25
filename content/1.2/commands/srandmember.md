---
title: "SRANDMEMBER"
description: "Return random members without removing; negative count allows repeats"
version: "1.2"
command: "SRANDMEMBER"
syntax: "SRANDMEMBER key [count]"
group: "set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "set", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SRANDMEMBER key [count]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@set`, `@slow`
<!-- generated: end -->
## Description

Return random members without removing; negative count allows repeats
