---
title: "UNLINK"
description: "Deletes the given keys, like DEL, but frees large values in the background."
version: "1.1"
command: "UNLINK"
syntax: "UNLINK key [key ...]"
group: "generic"
since: "1.1.0"
arity: -2
flags: ["fast", "write"]
acl_categories: ["fast", "generic", "keyspace", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
UNLINK key [key ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@generic`, `@keyspace`, `@write`
<!-- generated: end -->
Deletes the given keys, like [`DEL`](del.md), but frees large values in the background.

A value that takes more than 64 units of work to free goes to a background thread; the key is gone at once either way. A unit is a list, set, sorted-set or hash element, a JSON field, a stream node, a time series sample. Strings are always freed at once. `INFO` counts what is freed this way in `lazyfree_pending_objects` and `lazyfreed_objects`.

Background freeing is new in 1.1.1. In 1.1.0, `UNLINK` was the same as `DEL`.

## Reply

- The number of keys deleted.

## Examples

```
> SET a 1
OK
> UNLINK a missing
(integer) 1
```
