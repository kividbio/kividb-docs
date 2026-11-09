---
title: "CLUSTER SAVECONFIG"
description: "Writes the node's topology to nodes.conf (cluster-config-file) now."
version: "1.2"
command: "CLUSTER SAVECONFIG"
syntax: "CLUSTER SAVECONFIG"
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
CLUSTER SAVECONFIG
```

**Available since:** 1.1.0
<!-- generated: end -->
Writes this node's view of the cluster to its cluster config file now: its own ID, the other nodes it knows, who owns which slot, and the epochs. The file is [`cluster-config-file`](../reference/configuration.md#cluster-config-file), `nodes.conf` in the node's working directory by default, and it is how the node finds the cluster again when it restarts.

The node also writes the file on its own, after each change it makes to the topology and as it hears of changes from the others, so you rarely need this command. Use it to make sure the file on disk is current, for example before copying the node's directory, or to check that the node can still write it: a failed write is returned as an error. The file is written to `nodes.conf.tmp` first and then renamed into place, so a crash never leaves half a file.

## Reply

`OK`.

## Errors

- `ERR` followed by the file system error, when the file cannot be written.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

```
> CLUSTER SAVECONFIG
OK
```

The file it writes has the format of [`CLUSTER NODES`](cluster-nodes.md), plus the epochs:

```
240000c7b26aff6822750277dedf276551ee0e64 127.0.0.1:7102@17102 myself,master - 0 0 3 connected 10923-16383
74cea35fa9a656f033023e9f6cb3d78ef2b1a95a 127.0.0.1:7100@17100 master - 1794254515538 1794254515539 1 connected 0-5460
...
vars currentEpoch 9 lastVoteEpoch 0
```
