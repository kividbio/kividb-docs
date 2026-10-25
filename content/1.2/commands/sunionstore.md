---
title: "SUNIONSTORE"
description: "Store the union in destination; returns count of members stored"
version: "1.2"
command: "SUNIONSTORE"
syntax: "SUNIONSTORE destination key [key ...]"
group: "set"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["set", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SUNIONSTORE destination key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@set`, `@slow`, `@write`
<!-- generated: end -->
## Description

Store the union in destination; returns count of members stored
