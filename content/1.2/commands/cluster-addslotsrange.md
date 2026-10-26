---
title: "CLUSTER ADDSLOTSRANGE"
description: "Like CLUSTER ADDSLOTS, for the ranges start to end, both included."
version: "1.2"
command: "CLUSTER ADDSLOTSRANGE"
syntax: "CLUSTER ADDSLOTSRANGE start end [start end ...]"
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
CLUSTER ADDSLOTSRANGE start end [start end ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Like [`CLUSTER ADDSLOTS`](cluster-addslots.md), for the ranges `start` to `end`, both included.

## Examples

```
> CLUSTER ADDSLOTSRANGE 0 8191
OK
```
