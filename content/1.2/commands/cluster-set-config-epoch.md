---
title: "CLUSTER SET-CONFIG-EPOCH"
description: "Sets this node's config epoch: the number its claims to slots carry, so that when two nodes claim one slot, the claim with the higher epoch wins."
version: "1.2"
command: "CLUSTER SET-CONFIG-EPOCH"
syntax: "CLUSTER SET-CONFIG-EPOCH epoch"
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
CLUSTER SET-CONFIG-EPOCH epoch
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets this node's config epoch: the number its claims to slots carry, so that when two nodes claim one slot, the claim with the higher epoch wins. Tools that build a cluster can give each new master a different epoch with it, so that none starts with a tie. You rarely need it by hand: when two masters have the same epoch, the one with the lower ID moves itself to a new one, as in Redis.

- `epoch`: a whole number, `0` or above.

It is accepted only on a fresh node, as in Redis: while it knows no other node and its config epoch is `0`; afterwards it is refused. If `epoch` is above the node's current epoch, the current epoch is raised to it too. [`CLUSTER INFO`](cluster-info.md) shows both, as `cluster_my_epoch` and `cluster_current_epoch`.

Before 1.2.1, it was accepted on a node that had already joined a cluster, as long as its config epoch was still `0`, and a negative epoch was `ERR value is not an integer or out of range`.

## Reply

`OK`.

## Errors

- `ERR Node config epoch is already non-zero`.
- `ERR The user can assign a config epoch only when the node does not know any other node.`
- `ERR Invalid config epoch specified: n`: `epoch` is negative.
- `ERR value is not an integer or out of range`: `epoch` is not a number.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER SET-CONFIG-EPOCH 1
OK
> CLUSTER SET-CONFIG-EPOCH 2
(error) ERR Node config epoch is already non-zero
> CLUSTER SET-CONFIG-EPOCH -1
(error) ERR Invalid config epoch specified: -1
```
