---
title: "CLUSTER DELSLOTS"
description: "Makes this node give up each slot."
version: "1.2"
command: "CLUSTER DELSLOTS"
syntax: "CLUSTER DELSLOTS slot [slot ...]"
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
CLUSTER DELSLOTS slot [slot ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node give up each `slot`. A slot that no node owns is not served: while there is one, `cluster_state` is `fail` and keyed commands are answered with `CLUSTERDOWN`, unless `cluster-require-full-coverage` is `no`.

## Examples

```
> CLUSTER DELSLOTS 8191
OK
```
