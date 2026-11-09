---
title: "CLUSTER GETKEYSINSLOT"
description: "Returns up to count of the keys this node holds in slot."
version: "1.2"
command: "CLUSTER GETKEYSINSLOT"
syntax: "CLUSTER GETKEYSINSLOT slot count"
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
CLUSTER GETKEYSINSLOT slot count
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns up to `count` of the keys this node holds in `slot`. Tools that move slots between masters use it to find the keys to send with [`MIGRATE`](migrate.md): `redis-cli --cluster reshard` asks for a batch, moves it, and asks again until the slot is empty. [`CLUSTER COUNTKEYSINSLOT`](cluster-countkeysinslot.md) counts them.

- `slot`: a slot number from `0` to `16383`.
- `count`: the most keys to return, `1` or more.

The keys come in no particular order. Like `CLUSTER COUNTKEYSINSLOT`, it looks at this node's memory only, and walks every key of the node until it has `count` of them, so on a node with many keys it is slow; see the known issue in [Adding a master and moving slots](../guides/cluster.md#adding-a-master-and-moving-slots). Unlike Redis, it also works on a server that is not a cluster node.

A `count` of `0` returns one key, if the slot has any, where Redis returns an empty array. Ask for `1` or more.

## Reply

An array of key names; an empty array if the node holds none in the slot.

## Errors

- `ERR Invalid slot n, must be between 0 and 16383`.
- `ERR value is not an integer or out of range`: `slot` is not a number, or `count` is negative or not a number.

## Examples

```
> MSET user:7 v {user:7}:cart 3 {user:7}:orders 7
OK
> CLUSTER GETKEYSINSLOT 2780 10
1) "user:7"
2) "{user:7}:cart"
3) "{user:7}:orders"
> CLUSTER GETKEYSINSLOT 2780 2
1) "user:7"
2) "{user:7}:cart"
> CLUSTER GETKEYSINSLOT 0 10
(empty array)
```
