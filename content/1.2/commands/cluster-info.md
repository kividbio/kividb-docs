---
title: "CLUSTER INFO"
description: "Returns the node's view of the cluster as field:value lines: whether the cluster is up (cluster_state), how many slots are assigned and how many of those are failing, the nodes it knows, the number o…"
version: "1.2"
command: "CLUSTER INFO"
syntax: "CLUSTER INFO"
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
CLUSTER INFO
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the node's view of the cluster as `field:value` lines: whether the cluster is up (`cluster_state`), how many slots are assigned and how many of those are failing, the nodes it knows, the number of masters serving slots (`cluster_size`), the epochs, and the bus messages sent and received.

`cluster_state` is `fail` while a slot has no owner, or its owner has failed, unless `cluster-require-full-coverage` is `no`.

## Examples

```
> CLUSTER INFO
cluster_enabled:1
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:3
cluster_size:2
cluster_current_epoch:1
cluster_my_epoch:1
cluster_stats_messages_sent:18
cluster_stats_messages_received:18
total_cluster_links_buffer_limit_exceeded:0
```
