---
title: "CLUSTER"
description: "List replicas of a given master."
version: "1.1"
command: "CLUSTER"
syntax: "CLUSTER REPLICAS master-id"
group: "cluster"
since: "1.1.0"
arity: -2
flags: []
acl_categories: ["cluster", "slow"]
history: []
subcommands: ["CLUSTER ADDSLOTS", "CLUSTER ADDSLOTSRANGE", "CLUSTER BUMPEPOCH", "CLUSTER COUNT-FAILURE-REPORTS", "CLUSTER COUNTKEYSINSLOT", "CLUSTER DELSLOTS", "CLUSTER DELSLOTSRANGE", "CLUSTER FAILOVER", "CLUSTER FLUSHSLOTS", "CLUSTER FORGET", "CLUSTER GETKEYSINSLOT", "CLUSTER HELP", "CLUSTER INFO", "CLUSTER KEYSLOT", "CLUSTER LINKS", "CLUSTER MEET", "CLUSTER MIGRATION", "CLUSTER MYID", "CLUSTER MYSHARDID", "CLUSTER NODES", "CLUSTER REPLICAS", "CLUSTER REPLICATE", "CLUSTER RESET", "CLUSTER SAVECONFIG", "CLUSTER SET-CONFIG-EPOCH", "CLUSTER SETSLOT", "CLUSTER SHARDS", "CLUSTER SLAVES", "CLUSTER SLOT-STATS", "CLUSTER SLOTS"]
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLUSTER REPLICAS master-id
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@slow`

Subcommands: [CLUSTER ADDSLOTS](cluster-addslots.md), [CLUSTER ADDSLOTSRANGE](cluster-addslotsrange.md), [CLUSTER BUMPEPOCH](cluster-bumpepoch.md), [CLUSTER COUNT-FAILURE-REPORTS](cluster-count-failure-reports.md), [CLUSTER COUNTKEYSINSLOT](cluster-countkeysinslot.md), [CLUSTER DELSLOTS](cluster-delslots.md), [CLUSTER DELSLOTSRANGE](cluster-delslotsrange.md), [CLUSTER FAILOVER](cluster-failover.md), [CLUSTER FLUSHSLOTS](cluster-flushslots.md), [CLUSTER FORGET](cluster-forget.md), [CLUSTER GETKEYSINSLOT](cluster-getkeysinslot.md), [CLUSTER HELP](cluster-help.md), [CLUSTER INFO](cluster-info.md), [CLUSTER KEYSLOT](cluster-keyslot.md), [CLUSTER LINKS](cluster-links.md), [CLUSTER MEET](cluster-meet.md), [CLUSTER MIGRATION](cluster-migration.md), [CLUSTER MYID](cluster-myid.md), [CLUSTER MYSHARDID](cluster-myshardid.md), [CLUSTER NODES](cluster-nodes.md), [CLUSTER REPLICAS](cluster-replicas.md), [CLUSTER REPLICATE](cluster-replicate.md), [CLUSTER RESET](cluster-reset.md), [CLUSTER SAVECONFIG](cluster-saveconfig.md), [CLUSTER SET-CONFIG-EPOCH](cluster-set-config-epoch.md), [CLUSTER SETSLOT](cluster-setslot.md), [CLUSTER SHARDS](cluster-shards.md), [CLUSTER SLAVES](cluster-slaves.md), [CLUSTER SLOT-STATS](cluster-slot-stats.md), [CLUSTER SLOTS](cluster-slots.md)
<!-- generated: end -->
## Description

List replicas of a given master. Aliases.
