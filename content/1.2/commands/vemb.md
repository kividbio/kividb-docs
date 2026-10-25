---
title: "VEMB"
description: "Return the vector as an array of float strings; with RAW, return raw little-endian FP32 bytes"
version: "1.2"
command: "VEMB"
syntax: "VEMB key element [RAW]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["read", "slow", "vector"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VEMB key element [RAW]
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@vector`
<!-- generated: end -->
## Description

Return the vector as an array of float strings; with `RAW`, return raw little-endian FP32 bytes
