---
title: "MEMORY MALLOC-STATS"
description: "Returns the memory allocator's statistics, in Redis."
version: "1.2"
command: "MEMORY MALLOC-STATS"
syntax: "MEMORY MALLOC-STATS"
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
MEMORY MALLOC-STATS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the memory allocator's statistics, in Redis. KiviDB is not built with jemalloc, and replies as Redis does then: `Stats not supported for the current allocator`. Before 1.2, it returned a fixed piece of XML.

[`INFO memory`](info.md) and [`MEMORY STATS`](memory-stats.md) give what KiviDB measures.

## Examples

```
> MEMORY MALLOC-STATS
"Stats not supported for the current allocator"
```
