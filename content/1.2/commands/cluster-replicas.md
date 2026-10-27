---
title: "CLUSTER REPLICAS"
description: "Returns the replicas of the master master-id, each as a CLUSTER NODES line."
version: "1.2"
command: "CLUSTER REPLICAS"
syntax: "CLUSTER REPLICAS master-id"
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
CLUSTER REPLICAS master-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the replicas of the master `master-id`, each as a [`CLUSTER NODES`](cluster-nodes.md) line.

The reply is an array, one string a replica, and an empty array for a master without replicas. `CLUSTER SLAVES` is the same. Before 1.2, both replied with one string, the lines joined by newlines.

## Examples

```
> CLUSTER REPLICAS 5c41f1bfc4f9d9f6d69358bb34269e9f98279c72
1) "60f37104e07b4024b37f335d52188a29cecf46dd 127.0.0.1:7311@17311 slave 5c41f1bfc4f9d9f6d69358bb34269e9f98279c72 1793114623408 1793114623413 2 connected"
```
