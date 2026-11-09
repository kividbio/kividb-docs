---
title: "TOUCH"
description: "Counts how many of the given keys exist."
version: "1.2"
command: "TOUCH"
syntax: "TOUCH key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "readonly"]
acl_categories: ["fast", "generic", "keyspace", "read"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
TOUCH key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@read`
<!-- generated: end -->
Marks the given keys as used, and returns how many of them exist. It is for keeping keys that matter from being evicted: under an LRU `maxmemory-policy`, `TOUCH` resets each key's idle time, as a read would, without sending its value back; under an LFU one, it counts as a use. [Memory](../guides/memory.md#at-the-limit) explains how eviction picks keys.

Keys that do not exist, or whose time to live has run out, are skipped and not counted. A key named twice is counted twice, as in [`EXISTS`](exists.md). `TOUCH` does not change a key's value or its time to live. Unlike `EXISTS`, which only asks, `TOUCH` counts as a use; under a policy that does not go by use, such as the default `noeviction`, nothing is recorded and the two are the same.

## Reply

The number of keys that exist, counting repeats, as an integer.

## Examples

Under `allkeys-lru`:

```
> SET a 1
OK
> OBJECT IDLETIME a          (some seconds later)
(integer) 3
> TOUCH a missing a
(integer) 2
> OBJECT IDLETIME a
(integer) 0
```
