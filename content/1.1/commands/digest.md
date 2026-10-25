---
title: "DIGEST"
description: "Return the digest that IFDEQ / IFDNE compare against: the XXH3 64-bit hash of the string value, as 16 hex digits (the same value Redis returns); nil for a missing key"
version: "1.1"
command: "DIGEST"
syntax: "DIGEST key"
group: "string"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
DIGEST key
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
## Description

Return the digest that `IFDEQ` / `IFDNE` compare against: the XXH3 64-bit hash of the string value, as 16 hex digits (the same value Redis returns); nil for a missing key
