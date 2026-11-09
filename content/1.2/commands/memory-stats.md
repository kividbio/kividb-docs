---
title: "MEMORY STATS"
description: "Returns the server's memory figures as name-value pairs, with the same names as Redis, for tools that read them:"
version: "1.2"
command: "MEMORY STATS"
syntax: "MEMORY STATS"
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
MEMORY STATS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the server's memory figures as name-value pairs, with the same names as Redis, for tools that read them:

- `used_memory`, `used_memory_rss`, `used_memory_peak` and `used_memory_vsize`, each also as `*_human`, and `used_memory_peak_perc`, `used_memory` as a share of the peak.
- `mem_fragmentation_ratio` and `mem_fragmentation_bytes`: RSS against `used_memory`.
- `active_defrag_running`, `lazyfree_pending_objects` and `lazyfreed_objects`.

The `allocator_*` and `rss_overhead_*` figures are always `1.0` and `0`: KiviDB does not use jemalloc, which reports them in Redis. [`INFO memory`](info.md) gives these and more.

## Examples

```
> MEMORY STATS
 1) "used_memory"
 2) "2101726"
 3) "used_memory_human"
 4) "2.00M"
 5) "used_memory_rss"
 6) "18862080"
...
39) "lazyfreed_objects"
40) "4"
```
