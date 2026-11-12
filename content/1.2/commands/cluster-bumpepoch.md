---
title: "CLUSTER BUMPEPOCH"
description: "Gives this node a config epoch above every epoch it knows of, so that its claims to its slots win over older ones, and replies BUMPED and the new epoch."
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
Gives this node a config epoch above every epoch it knows of, so that its claims to its slots win over older ones, and replies `BUMPED` and the new epoch. When the node's config epoch is already the highest, and not `0`, it changes nothing and replies `STILL` and the epoch. The config epoch is `cluster_my_epoch` in [`CLUSTER INFO`](cluster-info.md) and the epoch column of [`CLUSTER NODES`](cluster-nodes.md); the current epoch, `cluster_current_epoch`, is raised with it.

That is as in Redis, since 1.2.1. In 1.2.0 it raised only the current epoch, left the config epoch as it was, and always replied `BUMPED`.

## Reply

`BUMPED` and the new epoch, or `STILL` and the epoch, as a status string.

## Errors

- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

On a node whose config epoch is not the highest, then on one whose is:

```
> CLUSTER INFO
"...cluster_current_epoch:3\r\ncluster_my_epoch:1\r\n..."
> CLUSTER BUMPEPOCH
BUMPED 4
> CLUSTER INFO
"...cluster_current_epoch:4\r\ncluster_my_epoch:4\r\n..."
```

```
> CLUSTER BUMPEPOCH
STILL 3
```
