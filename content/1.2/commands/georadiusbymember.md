---
title: "GEORADIUSBYMEMBER"
description: "GEORADIUS centred on a member of the index, not a position."
version: "1.2"
command: "GEORADIUSBYMEMBER"
syntax: "GEORADIUSBYMEMBER key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]"
group: "geospatial"
since: "1.1.0"
arity: -5
flags: ["movablekeys", "write"]
acl_categories: ["geo", "slow", "write"]
history: [{"release": "1.2.1", "change": "flags: added write; removed readonly; acl categories: added write; removed read"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUSBYMEMBER key member radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`

**History:**

- 1.2.1: flags: added write; removed readonly; acl categories: added write; removed read
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

With `STORE` or `STOREDIST` given more than once, the last destination is written, and the ACL checks every one; before 1.2 it checked only the first ([GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3)).

Like `GEORADIUS`, it is a write command since 1.2.1: with `STORE` or `STOREDIST` it needs write access to the destination, a read-only replica refuses it with `READONLY` even without them, and `GEORADIUSBYMEMBER_RO` or [`GEOSEARCH`](geosearch.md) is the way to read. See [`GEORADIUS`](georadius.md) and [GHSA-cg4w-p5w5-57w5](https://github.com/kividbio/kividb/security/advisories/GHSA-cg4w-p5w5-57w5).
