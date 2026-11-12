---
title: "EXISTS"
description: "Returns how many of the given keys exist."
version: "1.2"
command: "EXISTS"
syntax: "EXISTS key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "keyspace", "read"]
history: [{"release": "1.2.1", "change": "acl categories: removed generic"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
EXISTS key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@keyspace`, `@read`

**History:**

- 1.2.1: acl categories: removed generic
<!-- generated: end -->
Returns how many of the given keys exist. With one key the answer is `1` or `0`, so it serves as a yes-or-no test.

With several keys, each is counted every time it is named: `EXISTS a a` is `2` when `a` exists. To check that every key of a list exists, name each one once and compare the count with the number of keys.

A key of any type counts, a string holding `""` included. A key whose time to live has run out does not. `EXISTS` only asks: it does not count as a use of the key for an LRU or LFU [eviction policy](../guides/memory.md#at-the-limit), and leaves the key's [`OBJECT IDLETIME`](object-idletime.md) as it was. [`TOUCH`](touch.md) counts the same way and does mark the keys as used. [`TYPE`](type.md) tells a key's type as well, `none` for a missing one.

In a cluster, the keys must all be in one slot, or the command fails with `CROSSSLOT` ([Cluster](../guides/cluster.md#how-keys-are-placed)).

## Reply

The number of keys that exist, counting repeats, as an integer.

## Examples

```
> SET a 1
OK
> SET empty ""
OK
> EXISTS a
(integer) 1
> EXISTS a a missing
(integer) 2
> EXISTS a empty
(integer) 2
> EXISTS missing
(integer) 0
```
