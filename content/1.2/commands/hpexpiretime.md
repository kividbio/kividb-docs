---
title: "HPEXPIRETIME"
description: "Same as HEXPIRETIME but the timestamp is in milliseconds"
version: "1.2"
command: "HPEXPIRETIME"
syntax: "HPEXPIRETIME key FIELDS numfields field [field ...]"
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
HPEXPIRETIME key FIELDS numfields field [field ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@hash`, `@read`, `@slow`
<!-- generated: end -->
## Description

Same as `HEXPIRETIME` but the timestamp is in milliseconds
