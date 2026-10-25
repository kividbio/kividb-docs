---
title: "GEORADIUS_RO"
description: "Read-only variant of GEORADIUS; does not support STORE or STOREDIST"
version: "1.1"
command: "GEORADIUS_RO"
syntax: "GEORADIUS_RO key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]"
group: "geospatial"
since: "1.1.0"
arity: -6
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEORADIUS_RO key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Read-only variant of `GEORADIUS`; does not support `STORE` or `STOREDIST`
