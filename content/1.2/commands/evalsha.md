---
title: "EVALSHA"
description: "Execute a script already in the cache by SHA1"
version: "1.2"
command: "EVALSHA"
syntax: "EVALSHA sha1 numkeys key [key ...] arg [arg ...]"
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
EVALSHA sha1 numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
## Description

Execute a script already in the cache by SHA1
