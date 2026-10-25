---
title: "FCALL"
description: "Call a registered library function."
version: "1.1"
command: "FCALL"
syntax: "FCALL function_name numkeys key [key ...] arg [arg ...]"
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
FCALL function_name numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
## Description

Call a registered library function. It is held to the flags it was registered with: with `no-writes` it cannot write; at the memory limit it runs only if it has `allow-oom` or `no-writes`
