---
title: "GEORADIUSBYMEMBER_RO"
description: "GEORADIUSBYMEMBER without STORE or STOREDIST, for read-only replicas."
version: "1.2"
command: "GEORADIUSBYMEMBER_RO"
syntax: "GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["readonly"]
acl_categories: ["geo", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER_RO key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@read`, `@slow`
<!-- generated: end -->
[`GEORADIUSBYMEMBER`](georadiusbymember.md) without `STORE` or `STOREDIST`, for read-only replicas. `STORE` is refused with `ERR syntax error`.

## Examples

```
> GEORADIUSBYMEMBER_RO g Palermo 200 km
1) "Palermo"
2) "Catania"
```
