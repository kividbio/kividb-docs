---
title: "CLUSTER REPLICATE"
description: "Makes this node a replica of the master master-id."
version: "1.1"
command: "CLUSTER REPLICATE"
syntax: "CLUSTER REPLICATE master-id"
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
CLUSTER REPLICATE master-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node a replica of the master `master-id`. A node that owns slots is refused: give them up first, with [`CLUSTER DELSLOTS`](cluster-delslots.md) or [`CLUSTER FLUSHSLOTS`](cluster-flushslots.md).

## Reply

- `OK`.
- `ERR To set a master as replica it must be empty of slots (count owned)`.

## Examples

```
> CLUSTER REPLICATE b2744aeada9b56dd000f101f31447a33a15c9b08
OK
```
