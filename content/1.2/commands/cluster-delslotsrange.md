---
title: "CLUSTER DELSLOTSRANGE"
description: "Like CLUSTER DELSLOTS, for the ranges start to end, both included."
version: "1.2"
command: "CLUSTER DELSLOTSRANGE"
syntax: "CLUSTER DELSLOTSRANGE start end [start end ...]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER DELSLOTSRANGE start end [start end ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Like [`CLUSTER DELSLOTS`](cluster-delslots.md), for the ranges `start` to `end`, both included.

## Examples

```
> CLUSTER DELSLOTSRANGE 8000 8010
OK
```
