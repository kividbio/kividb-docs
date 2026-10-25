---
title: "EVALSHA_RO"
description: "Read-only EVALSHA"
version: "1.2"
command: "EVALSHA_RO"
syntax: "EVALSHA_RO sha1 numkeys key [key ...] arg [arg ...]"
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
EVALSHA_RO sha1 numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
## Description

Read-only `EVALSHA`
