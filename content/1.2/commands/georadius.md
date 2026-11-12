---
title: "GEORADIUS"
description: "Returns the members of the geospatial index at key within radius of a longitude and latitude."
version: "1.2"
command: "GEORADIUS"
syntax: "GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]"
group: "geospatial"
since: "1.1.0"
arity: -6
flags: ["movablekeys", "write"]
acl_categories: ["geo", "slow", "write"]
history: [{"release": "1.2.1", "change": "flags: added write; removed readonly; acl categories: added write; removed read"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
GEORADIUS key longitude latitude radius <M | KM | FT | MI> [WITHCOORD] [WITHDIST] [WITHHASH] [COUNT count [ANY]] [ASC | DESC] [STORE key | STOREDIST key]
```

**Available since:** 1.1.0 · **ACL categories:** `@geo`, `@slow`, `@write`

**History:**

- 1.2.1: flags: added write; removed readonly; acl categories: added write; removed read
<!-- generated: end -->
Returns the members of the geospatial index at `key` within `radius` of a longitude and latitude. It is the older form of [`GEOSEARCH`](geosearch.md) `FROMLONLAT ... BYRADIUS`, with the same `WITH`, `COUNT` and `ASC`/`DESC` options, and `STORE key` or `STOREDIST key` to store the result as [`GEOSEARCHSTORE`](geosearchstore.md) does.

## Examples

```
> GEOADD g 13.361389 38.115556 Palermo 15.087269 37.502669 Catania
(integer) 2
> GEORADIUS g 15 37 200 km WITHDIST ASC
1) 1) "Catania"
   2) "56.4413"
2) 1) "Palermo"
   2) "190.4424"
```

With `STORE` or `STOREDIST` given more than once, the last destination is written, and the ACL checks every one; before 1.2 it checked only the first ([GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3)).

Since it can write, `GEORADIUS` is a write command, in `@write` and not `@read`, as in Redis. With `STORE` or `STOREDIST` it needs write access to the destination: a user with read-only key rights (`%R~*`), or with `+@read` alone, gets `NOPERM`, and `min-replicas-to-write`, the out-of-memory refusal and [`aof-ack-after-write`](../reference/configuration.md#aof-ack-after-write) apply to it as to other writes. A read-only replica refuses it with `READONLY`, with or without `STORE`. To read, from a replica or as a user that may only read, use `GEORADIUS_RO` or [`GEOSEARCH`](geosearch.md). That is since 1.2.1, which fixes [GHSA-cg4w-p5w5-57w5](https://github.com/kividbio/kividb/security/advisories/GHSA-cg4w-p5w5-57w5): before it, a user that could only read could write the destination, and a replica ran it when it did not store.

```
> ACL SETUSER reporting on >report-password %R~* +@all
OK
> AUTH reporting report-password
OK
> GEORADIUS g 15 37 200 km
1) "Palermo"
2) "Catania"
> GEORADIUS g 15 37 200 km STORE nearby
(error) NOPERM User reporting has no permissions to access the 'nearby' key
```
