---
title: "GEORADIUSBYMEMBER"
description: "GEORADIUS centred on a member of the index, not a position."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
[`GEORADIUS`](georadius.md) centred on a member of the index, not a position.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEORADIUSBYMEMBER g Palermo 200 km
1) "Palermo"
2) "Catania"
```
