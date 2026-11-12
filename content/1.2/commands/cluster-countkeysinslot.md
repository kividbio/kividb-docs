---
title: "CLUSTER COUNTKEYSINSLOT"
description: "Returns the number of keys this node holds in slot."
version: "1.2"
command: "CLUSTER COUNTKEYSINSLOT"
syntax: "CLUSTER COUNTKEYSINSLOT slot"
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
CLUSTER COUNTKEYSINSLOT slot
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the number of keys this node holds in `slot`. Use it to check how many keys a slot has before or during a move between masters, or to confirm a slot is empty before [`CLUSTER DELSLOTS`](cluster-delslots.md). [`CLUSTER GETKEYSINSLOT`](cluster-getkeysinslot.md) returns the keys themselves, and [`CLUSTER KEYSLOT`](cluster-keyslot.md) gives the slot of a key.

- `slot`: a slot number from `0` to `16383`.

It counts the keys in this node's memory only. A slot this node does not own normally has `0`; a replica counts the keys it holds for its master's slots. The count walks every key of the node, so it takes longer the more keys the node holds.

On a server that is not a cluster node it replies `ERR This instance has cluster support disabled`, as Redis does, since 1.2.1; 1.2.0 counted the keys that would hash to the slot.

## Reply

The number of keys, as an integer.

## Errors

- `ERR Invalid slot n, must be between 0 and 16383`.
- `ERR value is not an integer or out of range`: `slot` is not a number.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER KEYSLOT user:7
(integer) 2780
> MSET user:7 v {user:7}:cart 3 {user:7}:orders 7
OK
> CLUSTER COUNTKEYSINSLOT 2780
(integer) 3
> CLUSTER COUNTKEYSINSLOT 0
(integer) 0
> CLUSTER COUNTKEYSINSLOT 16384
(error) ERR Invalid slot 16384, must be between 0 and 16383
```
