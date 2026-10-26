---
title: "ARNEXT"
description: "Returns the index the next ARINSERT will use: 0 for a missing key, nil once the cursor has run past the last index."
version: "1.1"
command: "ARNEXT"
syntax: "ARNEXT key"
group: "array"
since: "1.1.0"
arity: -2
flags: ["readonly"]
acl_categories: ["array", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ARNEXT key
```

**Available since:** 1.1.0 · **ACL categories:** `@array`, `@read`, `@slow`
<!-- generated: end -->
Returns the index the next [`ARINSERT`](arinsert.md) will use: `0` for a missing key, `nil` once the cursor has run past the last index.
