---
title: "GEORADIUSBYMEMBER_RO"
description: "Read-only variant of GEORADIUSBYMEMBER; does not support STORE or STOREDIST"
version: "1.1"
command: "GEORADIUSBYMEMBER_RO"
syntax: "GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Read-only variant of `GEORADIUSBYMEMBER`; does not support `STORE` or `STOREDIST`
