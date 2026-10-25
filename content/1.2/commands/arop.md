---
title: "AROP"
description: "Aggregate over non-empty elements in a range."
version: "1.2"
command: "AROP"
syntax: "AROP key start end <SUM | MIN | MAX | AND | OR | XOR | MATCH value | USED>"
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
AROP key start end <SUM | MIN | MAX | AND | OR | XOR | MATCH value | USED>
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
## Description

Aggregate over non-empty elements in a range. SUM/MIN/MAX return bulk strings and reply nil when the range holds no numeric elements; AND/OR/XOR/MATCH/USED return integers
