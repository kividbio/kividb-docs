---
title: "CLUSTER HELP"
description: "Lists the CLUSTER subcommands, with a line or two on what each does, as Redis does."
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
Lists the `CLUSTER` subcommands, with a line or two on what each does, as Redis does. An unknown subcommand gets `ERR unknown subcommand '<name>'. Try CLUSTER HELP.`.

It is since 1.2.1. In 1.2.0 a cluster node answered it with `ERR Unknown CLUSTER subcommand 'HELP'`. As every cluster-only subcommand, it is refused on a server that is not a cluster node.

The subcommands are also listed, each with a link to its page, under [`CLUSTER`](cluster.md). For running a cluster, from creating one to failover, see the [Cluster guide](../guides/cluster.md).

## Reply

An array of simple strings: a line for each subcommand and its arguments, each followed by lines that describe it, indented.

## Examples

On a cluster node:

```
> CLUSTER HELP
 1) CLUSTER <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) COUNTKEYSINSLOT <slot>
 3)     Return the number of keys in <slot>.
 4) GETKEYSINSLOT <slot> <count>
 5)     Return key names stored by current node in a slot.
...
61)     Start, monitor and cancel slot migration.
62) HELP
63)     Print this help.
> CLUSTER FOO
(error) ERR unknown subcommand 'FOO'. Try CLUSTER HELP.
```

On a server started without `cluster-enabled yes`:

```
> CLUSTER HELP
(error) ERR This instance has cluster support disabled
```
