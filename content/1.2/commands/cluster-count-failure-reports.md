---
title: "CLUSTER COUNT-FAILURE-REPORTS"
description: "Returns how many other masters currently report node-id as failing."
version: "1.2"
command: "CLUSTER COUNT-FAILURE-REPORTS"
syntax: "CLUSTER COUNT-FAILURE-REPORTS node-id"
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
CLUSTER COUNT-FAILURE-REPORTS node-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many other masters currently report `node-id` as failing. Use it to see why a node is, or is not yet, marked `fail` in [`CLUSTER NODES`](cluster-nodes.md).

A node that gets no answer from another for [`cluster-node-timeout`](../reference/configuration.md#cluster-node-timeout) milliseconds suspects it (`fail?`), and says so in its heartbeats. Each node keeps the reports it hears from masters; reports from replicas are not counted, and neither is the node's own suspicion. A report counts for twice the node timeout after it was last made. When the reports, plus this node's own suspicion if it is a master, reach a majority of the slot-owning masters, this node marks the suspect `fail` and tells the others. If the suspect is a master, one of its replicas then takes its place. See [Failover](../guides/cluster.md#failover).

The count is this node's own view, so it can differ from node to node, and it drops back to `0` once the node answers again.

## Reply

The number of masters reporting the node, as an integer. A well-formed ID of a node this node does not know also gets `0`, where Redis replies `ERR Unknown node`.

## Errors

- `ERR Invalid node id`: not 40 hexadecimal characters.
- `ERR This instance has cluster support disabled`: the server is not a cluster node.

## Examples

A replica stopped, in a cluster of three masters and a 3-second node timeout, asked on each master a few seconds later:

```
> CLUSTER COUNT-FAILURE-REPORTS 95dc5ee672adb953ccc7fe76c427f5083b7c9b4b
(integer) 2
```

After the replica is back:

```
> CLUSTER COUNT-FAILURE-REPORTS 95dc5ee672adb953ccc7fe76c427f5083b7c9b4b
(integer) 0
> CLUSTER COUNT-FAILURE-REPORTS abc
(error) ERR Invalid node id
```
