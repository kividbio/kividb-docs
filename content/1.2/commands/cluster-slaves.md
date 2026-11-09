---
title: "CLUSTER SLAVES"
description: "Another name for CLUSTER REPLICAS, which Redis deprecates."
version: "1.2"
command: "CLUSTER SLAVES"
syntax: "CLUSTER SLAVES master-id"
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
CLUSTER SLAVES master-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the replicas of the master `master-id`, each as a [`CLUSTER NODES`](cluster-nodes.md) line. It is the old name of [`CLUSTER REPLICAS`](cluster-replicas.md), which Redis deprecates, and it behaves the same way: kept for older tools and clients, while new code should use `CLUSTER REPLICAS`.

- `master-id`: the master's node ID, as [`CLUSTER MYID`](cluster-myid.md) on it or `CLUSTER NODES` shows it.

## Reply

An array, one string a replica; an empty array for a master without replicas. Before 1.2, the reply was one string, the lines joined by newlines.

## Errors

- `ERR Unknown node`: this node does not know `master-id`.
- `ERR Invalid node id`: not 40 hexadecimal characters.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER SLAVES 74cea35fa9a656f033023e9f6cb3d78ef2b1a95a
1) "95dc5ee672adb953ccc7fe76c427f5083b7c9b4b 127.0.0.1:7103@17103 slave 74cea35fa9a656f033023e9f6cb3d78ef2b1a95a 1794254390492 1794254390514 9 connected"
> CLUSTER SLAVES 240000c7b26aff6822750277dedf276551ee0e64
(empty array)
> CLUSTER SLAVES 0000000000000000000000000000000000000000
(error) ERR Unknown node
```
