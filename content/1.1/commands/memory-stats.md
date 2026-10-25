---
title: "MEMORY STATS"
description: "Returns memory figures as name-value pairs: used_memory, used_memory_rss, used_memory_peak and others."
version: "1.1"
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
Returns memory figures as name-value pairs: `used_memory`, `used_memory_rss`, `used_memory_peak` and others.

## Examples

```
> MEMORY STATS
1) "used_memory"
2) "1653856"
3) "used_memory_human"
4) "1.58M"
5) "used_memory_rss"
6) "16867328"
...
```
