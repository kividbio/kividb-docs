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

It removes any slot this node has assigned, also one another node owns, and the slot's `IMPORTING` state, as Redis does; `redis-cli --cluster fix` relies on it to close a slot that an interrupted reshard left open. A slot that is not assigned is refused, and then nothing changes. For two seconds after, a peer's claim does not give the node the slot back. Before 1.2, a slot owned by another node was refused.
