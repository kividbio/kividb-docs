---
title: "CLUSTER FLUSHSLOTS"
description: "Makes this node give up every slot it owns, as CLUSTER DELSLOTS of each."
version: "1.1"
command: "CLUSTER FLUSHSLOTS"
syntax: "CLUSTER FLUSHSLOTS"
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
CLUSTER FLUSHSLOTS
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node give up every slot it owns, as [`CLUSTER DELSLOTS`](cluster-delslots.md) of each.

## Examples

```
> CLUSTER FLUSHSLOTS
OK
```
