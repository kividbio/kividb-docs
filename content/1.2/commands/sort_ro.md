---
title: "SORT_RO"
description: "SORT without STORE: it only reads, so it can be sent to a read-only replica."
version: "1.2"
command: "SORT_RO"
syntax: "SORT_RO key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["movablekeys", "readonly"]
acl_categories: ["generic", "keyspace", "read", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SORT_RO key [BY pattern] [LIMIT offset count] [GET pattern [...]] [ASC|DESC] [ALPHA]
```

**Available since:** 1.1.0 · **ACL categories:** `@generic`, `@keyspace`, `@read`, `@slow`
<!-- generated: end -->
[`SORT`](sort.md) without `STORE`: it only reads, so it can be sent to a read-only replica.

## Reply

- The sorted elements, or what `GET` reads.
- `ERR syntax error` if `STORE` is given.

## Examples

```
> RPUSH nums 3 1 2
(integer) 3
> SORT_RO nums
1) "1"
2) "2"
3) "3"
```

## ACL

A `BY` pattern with a `*`, and any `GET` other than `GET #`, read the keys the pattern names, so they need read access to every key, as in Redis. A user whose ACL is limited to some keys gets `ERR BY option of SORT denied due to insufficient ACL permissions.` or `ERR GET option of SORT denied due to insufficient ACL permissions.`; `BY nosort` and `GET #` need nothing more. Before 1.2, such a user could read any key this way ([GHSA-6rw7-4fcr-r6j3](https://github.com/kividbio/kividb/security/advisories/GHSA-6rw7-4fcr-r6j3)).
