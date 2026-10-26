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

## Known issue

On Linux it always reports high fragmentation: the ratio it reads, `mem_fragmentation_ratio`, is the process's virtual size over its resident size, not Redis's. Filed as [kividb#152](https://github.com/kividbio/kividb/issues/152).

## Examples

```
> MEMORY DOCTOR
Sam, I love your taste in T-shirts, but your memory is just fine.
```
