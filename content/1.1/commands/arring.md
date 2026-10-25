---
title: "ARRING"
description: "Insert into a ring buffer of size, wrapping at size so newer values overwrite older ones; shrinking size truncates."
version: "1.1"
command: "ARRING"
syntax: "ARRING key size value [value ...]"
group: "array"
since: "1.1.0"
arity: -2
flags: ["write"]
acl_categories: ["array", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
ARRING key size value [value ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@slow`, `@write`
<!-- generated: end -->
## Description

Insert into a ring buffer of `size`, wrapping at `size` so newer values overwrite older ones; shrinking `size` truncates. Returns the last index written
