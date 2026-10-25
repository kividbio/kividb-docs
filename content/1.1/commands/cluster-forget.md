---
title: "CLUSTER FORGET"
description: "Remove a node from the routing table."
version: "1.1"
command: "CLUSTER FORGET"
syntax: "CLUSTER FORGET node-id"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLUSTER FORGET node-id
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Remove a node from the routing table. Slots owned by the forgotten node become unassigned. The node is refused re-admission for 60 seconds, so gossip from a node that has not been told yet does not bring it back.
