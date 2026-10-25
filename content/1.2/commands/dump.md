---
title: "DUMP"
description: "Serialize the value at key to a binary string in KiviDB's snapshot format with a 10-byte CRC64 envelope; returns nil if key missing or expired; TimeSeries and VectorSet keys are not portable"
version: "1.2"
command: "DUMP"
syntax: "DUMP key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["readonly"]
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
DUMP key
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
## Description

Serialize the value at key to a binary string in KiviDB's snapshot format with a 10-byte CRC64 envelope; returns nil if key missing or expired; TimeSeries and VectorSet keys are not portable
