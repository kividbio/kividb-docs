---
title: "GEORADIUSBYMEMBER"
description: "Query members within a radius of an existing member; supports STORE and STOREDIST; AOF-logged when storing"
version: "1.1"
command: "GEORADIUSBYMEMBER"
syntax: "GEORADIUSBYMEMBER key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["movablekeys", "readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Query members within a radius of an existing member; supports `STORE` and `STOREDIST`; AOF-logged when storing
