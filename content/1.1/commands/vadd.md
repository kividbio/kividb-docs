---
title: "VADD"
description: "Add or update an element with its vector; FP32 accepts raw little-endian bytes, VALUES n accepts space-separated floats; returns 1 if new, 0 if updated; AOF-logged"
version: "1.1"
command: "VADD"
syntax: "VADD key [REDUCE dim] [DISTANCE L2|COSINE|INNERPRODUCT] (FP32 | VALUES num) vector element [SETATTR json] [NOQUANT|Q8|BIN] [EF n] [M n]"
group: "vector-set"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["slow", "vector", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
VADD key [REDUCE dim] [DISTANCE L2|COSINE|INNERPRODUCT] (FP32 | VALUES num) vector element [SETATTR json] [NOQUANT|Q8|BIN] [EF n] [M n]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@vector`, `@write`
<!-- generated: end -->
## Description

Add or update an element with its vector; `FP32` accepts raw little-endian bytes, `VALUES n` accepts space-separated floats; returns 1 if new, 0 if updated; AOF-logged
