---
title: "CLUSTER BUMPEPOCH"
description: "Increments the cluster's current epoch and gives it to this node, so that this node's claims to its slots win over older ones."
version: "1.2"
command: "CLUSTER BUMPEPOCH"
syntax: "CLUSTER BUMPEPOCH"
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
CLUSTER BUMPEPOCH
```

**Available since:** 1.1.0
<!-- generated: end -->
Raises this node's current epoch to one above the highest epoch it knows of, and returns it. The current epoch is the counter a node takes new epochs from, for a failover or a slot moved with [`CLUSTER SETSLOT`](cluster-setslot.md). [`CLUSTER INFO`](cluster-info.md) shows it as `cluster_current_epoch`.

In KiviDB 1.2 it does not change the node's own config epoch, `cluster_my_epoch` in `CLUSTER INFO` and the epoch column of [`CLUSTER NODES`](cluster-nodes.md). So on its own it does not make this node's claims to its slots win over older ones. Redis also gives the new epoch to the node as its config epoch, and replies `STILL` instead when the node's config epoch is already the highest; KiviDB always replies `BUMPED`.

## Reply

`BUMPED` and the new current epoch, as a status string.

## Errors

- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER INFO
"...cluster_current_epoch:9\r\ncluster_my_epoch:2\r\n..."
> CLUSTER BUMPEPOCH
BUMPED 10
> CLUSTER INFO
"...cluster_current_epoch:10\r\ncluster_my_epoch:2\r\n..."
```
