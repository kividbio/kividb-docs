---
title: "TYPE"
description: "Return the data type of a key: string, list, set, zset, hash, stream, ReJSON-RL, or none if missing/expired"
version: "1.2"
command: "TYPE"
syntax: "TYPE key"
group: "generic"
since: "1.1.0"
arity: 2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
TYPE key
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
## Description

Return the data type of a key: `string`, `list`, `set`, `zset`, `hash`, `stream`, `ReJSON-RL`, or `none` if missing/expired
