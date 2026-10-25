---
title: "GEORADIUS"
description: "Query members within a radius of explicit coordinates; STORE writes results to a destination key as a geo index; STOREDIST writes with distance scores; AOF-logged when STORE or STOREDIST is used"
version: "1.2"
command: "GEORADIUS"
syntax: "GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]"
group: "geospatial"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
## Description

Query members within a radius of explicit coordinates; `STORE` writes results to a destination key as a geo index; `STOREDIST` writes with distance scores; AOF-logged when `STORE` or `STOREDIST` is used
