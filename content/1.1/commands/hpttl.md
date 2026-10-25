---
title: "HPTTL"
description: "Same as HTTL but in milliseconds"
version: "1.1"
command: "HPTTL"
syntax: "HPTTL key FIELDS numfields field [field ...]"
group: "hash"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["hash", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HPTTL key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
## Description

Same as `HTTL` but in milliseconds
