---
title: "MEMORY PURGE"
description: "Asks the allocator to give the free memory it holds back to the system."
version: "1.2"
command: "MEMORY PURGE"
syntax: "MEMORY PURGE"
group: "server"
since: "1.1.0"
history: []
container: "MEMORY"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MEMORY PURGE
```

**Available since:** 1.1.0
<!-- generated: end -->
Asks the allocator to give the free memory it holds back to the system. On Linux it calls `malloc_trim`, which returns the free pages of the system allocator's heaps, where KiviDB keeps strings over about 4 KB and the elements of collections; `used_memory_rss` falls by what was freed. Elsewhere it does nothing.

It is rarely needed: KiviDB gives slabs back by itself, with active defrag, and after a large `FLUSHALL` or `FLUSHDB`. Try it when `used_memory_rss` stays well above `used_memory` after a large delete. [Memory](../guides/memory.md#what-deleting-gives-back) explains what is given back, and when.

## Reply

`OK`.

## Examples

```
> MEMORY PURGE
OK
```
