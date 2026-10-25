---
title: "RESTORE"
description: "Deserialize a value from a DUMP payload and store it at key; ttl is in milliseconds (0 = no expiry); REPLACE overwrites an existing key; ABSTTL treats ttl as a Unix timestamp in milliseconds; returns…"
version: "1.2"
command: "RESTORE"
syntax: "RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency]"
group: "generic"
since: "1.1.0"
arity: -4
flags: ["write"]
acl_categories: ["dangerous", "generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RESTORE key ttl serialized-value [REPLACE] [ABSTTL] [IDLETIME seconds] [FREQ frequency]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Deserialize a value from a `DUMP` payload and store it at key; ttl is in milliseconds (0 = no expiry); `REPLACE` overwrites an existing key; `ABSTTL` treats ttl as a Unix timestamp in milliseconds; returns `BUSYKEY` error if key exists without `REPLACE`
