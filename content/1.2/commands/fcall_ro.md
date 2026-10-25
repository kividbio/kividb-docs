---
title: "FCALL_RO"
description: "Read-only FCALL: refused for a function not registered with the no-writes flag"
version: "1.2"
command: "FCALL_RO"
syntax: "FCALL_RO function_name numkeys key [key ...] arg [arg ...]"
group: "scripting"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["scripting", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FCALL_RO function_name numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
## Description

Read-only `FCALL`: refused for a function not registered with the `no-writes` flag
