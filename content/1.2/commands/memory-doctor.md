---
title: "MEMORY DOCTOR"
description: "Returns a short report on memory health, in Redis's words."
version: "1.2"
command: "MEMORY DOCTOR"
syntax: "MEMORY DOCTOR"
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
MEMORY DOCTOR
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns a short report on memory health, in Redis's words.

It follows Redis's rules: nothing to say while `used_memory` is under 5 MB; high fragmentation when `mem_fragmentation_ratio` is above 1.4 and `used_memory_rss` is more than 10 MB over `used_memory`; a past peak when `used_memory_peak` is more than half as large again as `used_memory`. Before 1.2, the ratio it read was the process's virtual size over its resident size, and on Linux it always reported high fragmentation.

## Examples

```
> MEMORY DOCTOR
"Hi Sam, this instance is empty or is using very little memory, my issues detector can't be used in these conditions."
```

With 500,000 keys:

```
> MEMORY DOCTOR
"Sam, I love your taste in T-shirts, but your memory is just fine."
```
