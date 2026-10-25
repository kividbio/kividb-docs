---
title: "CLUSTER"
description: "Manages a cluster node: which slots it owns, which nodes it knows, its replicas, and the moving of slots between masters."
version: "1.2"
command: "CLUSTER"
syntax: "CLUSTER"
group: "cluster"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["cluster", "slow"]
history: []
subcommands: ["CLUSTER ADDSLOTS", "CLUSTER ADDSLOTSRANGE", "CLUSTER BUMPEPOCH", "CLUSTER COUNT-FAILURE-REPORTS", "CLUSTER COUNTKEYSINSLOT", "CLUSTER DELSLOTS", "CLUSTER DELSLOTSRANGE", "CLUSTER FAILOVER", "CLUSTER FLUSHSLOTS", "CLUSTER FORGET", "CLUSTER GETKEYSINSLOT", "CLUSTER HELP", "CLUSTER INFO", "CLUSTER KEYSLOT", "CLUSTER LINKS", "CLUSTER MEET", "CLUSTER MIGRATION", "CLUSTER MYID", "CLUSTER MYSHARDID", "CLUSTER NODES", "CLUSTER REPLICAS", "CLUSTER REPLICATE", "CLUSTER RESET", "CLUSTER SAVECONFIG", "CLUSTER SET-CONFIG-EPOCH", "CLUSTER SETSLOT", "CLUSTER SHARDS", "CLUSTER SLAVES", "CLUSTER SLOT-STATS", "CLUSTER SLOTS"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@slow`

Subcommands: [CLUSTER ADDSLOTS](cluster-addslots.md), [CLUSTER ADDSLOTSRANGE](cluster-addslotsrange.md), [CLUSTER BUMPEPOCH](cluster-bumpepoch.md), [CLUSTER COUNT-FAILURE-REPORTS](cluster-count-failure-reports.md), [CLUSTER COUNTKEYSINSLOT](cluster-countkeysinslot.md), [CLUSTER DELSLOTS](cluster-delslots.md), [CLUSTER DELSLOTSRANGE](cluster-delslotsrange.md), [CLUSTER FAILOVER](cluster-failover.md), [CLUSTER FLUSHSLOTS](cluster-flushslots.md), [CLUSTER FORGET](cluster-forget.md), [CLUSTER GETKEYSINSLOT](cluster-getkeysinslot.md), [CLUSTER HELP](cluster-help.md), [CLUSTER INFO](cluster-info.md), [CLUSTER KEYSLOT](cluster-keyslot.md), [CLUSTER LINKS](cluster-links.md), [CLUSTER MEET](cluster-meet.md), [CLUSTER MIGRATION](cluster-migration.md), [CLUSTER MYID](cluster-myid.md), [CLUSTER MYSHARDID](cluster-myshardid.md), [CLUSTER NODES](cluster-nodes.md), [CLUSTER REPLICAS](cluster-replicas.md), [CLUSTER REPLICATE](cluster-replicate.md), [CLUSTER RESET](cluster-reset.md), [CLUSTER SAVECONFIG](cluster-saveconfig.md), [CLUSTER SET-CONFIG-EPOCH](cluster-set-config-epoch.md), [CLUSTER SETSLOT](cluster-setslot.md), [CLUSTER SHARDS](cluster-shards.md), [CLUSTER SLAVES](cluster-slaves.md), [CLUSTER SLOT-STATS](cluster-slot-stats.md), [CLUSTER SLOTS](cluster-slots.md)
<!-- generated: end -->
Manages a cluster node: which slots it owns, which nodes it knows, its replicas, and the moving of slots between masters. A cluster node is started with `cluster-enabled yes`. On a standalone server the subcommands answer as for a node with no cluster: `CLUSTER INFO` gives `cluster_enabled:0`, and `CLUSTER SLOTS` an empty array.

The keyspace is split into 16384 slots; [`CLUSTER KEYSLOT`](cluster-keyslot.md) gives a key's. A command for a slot this node does not own is answered with `MOVED slot host:port`, the node that owns it, and a cluster client follows that. A cluster node has one database: [`SELECT`](select.md) of any but `0` is refused.
