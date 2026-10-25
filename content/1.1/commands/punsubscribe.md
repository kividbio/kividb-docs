---
title: "PUNSUBSCRIBE"
description: "Unsubscribe from patterns."
version: "1.1"
command: "PUNSUBSCRIBE"
syntax: "PUNSUBSCRIBE [pattern ...]"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: ["pubsub"]
acl_categories: ["pubsub", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PUNSUBSCRIBE [pattern ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Unsubscribe from patterns. With no arguments, unsubscribes from all patterns
