---
title: "COPY"
description: "Copy the value of source to destination without deleting source; REPLACE overwrites destination if it exists; DB copies to a different database; returns 1 if copied, 0 if skipped"
version: "1.2"
command: "COPY"
syntax: "COPY source destination [DB destination-db] [REPLACE]"
group: "generic"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["generic", "keyspace", "slow", "write"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
COPY source destination [DB destination-db] [REPLACE]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@slow`, `@write`
<!-- generated: end -->
## Description

Copy the value of source to destination without deleting source; `REPLACE` overwrites destination if it exists; `DB` copies to a different database; returns 1 if copied, 0 if skipped
