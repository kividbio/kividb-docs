---
title: "CLUSTER HELP"
description: "In Redis, CLUSTER HELP lists the CLUSTER subcommands and what each does."
version: "1.2"
command: "CLUSTER HELP"
syntax: "CLUSTER HELP"
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
CLUSTER HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
In Redis, `CLUSTER HELP` lists the `CLUSTER` subcommands and what each does. KiviDB 1.2.0 does not implement it: a cluster node answers it with an unknown-subcommand error, and a server that is not a cluster node with the error it gives every cluster-only subcommand. [`COMMAND DOCS`](command-docs.md) still lists it among the `CLUSTER` subcommands.

The subcommands are listed, each with a link to its page, under [`CLUSTER`](cluster.md). For running a cluster, from creating one to failover, see the [Cluster guide](../guides/cluster.md).

## Reply

An error, as below.

## Examples

On a cluster node:

```
> CLUSTER HELP
(error) ERR Unknown CLUSTER subcommand 'HELP'
```

On a server started without `cluster-enabled yes`:

```
> CLUSTER HELP
(error) ERR This instance has cluster support disabled
```
