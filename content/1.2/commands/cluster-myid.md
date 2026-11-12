---
title: "CLUSTER MYID"
description: "Returns this node's ID: 40 hexadecimal characters that name the node to the rest of the cluster."
version: "1.2"
command: "CLUSTER MYID"
syntax: "CLUSTER MYID"
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
CLUSTER MYID
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this node's ID: 40 hexadecimal characters that name the node to the rest of the cluster. The ID is what other `CLUSTER` commands take to name a node, such as [`CLUSTER REPLICATE`](cluster-replicate.md), [`CLUSTER FORGET`](cluster-forget.md) and [`CLUSTER SETSLOT`](cluster-setslot.md), and what the first column of [`CLUSTER NODES`](cluster-nodes.md) shows.

A node picks its ID at random the first time it starts, and keeps it in [`nodes.conf`](../reference/configuration.md#cluster-config-file), so it keeps the same ID across restarts. Keep that file with the node's data: a node started without it is a new node, with a new ID. [`CLUSTER RESET HARD`](cluster-reset.md) gives it a new one; `CLUSTER RESET SOFT` keeps it.

On a server that is not a cluster node it replies `ERR This instance has cluster support disabled`, as Redis does, since 1.2.1; 1.2.0 returned 40 zeros.

## Reply

The ID, as a string.

## Examples

```
> CLUSTER MYID
"5c7f6679196b15e2bd1a76761e2b41f47c5b30e2"
> CLUSTER RESET HARD
OK
> CLUSTER MYID
"c50daad0af30be1b0b7bc93c4c773958fa966c3a"
```

On a standalone server:

```
> CLUSTER MYID
(error) ERR This instance has cluster support disabled
```
