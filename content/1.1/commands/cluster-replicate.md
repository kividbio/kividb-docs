---
title: "CLUSTER REPLICATE"
description: "Configure this node as a replica."
version: "1.1"
command: "CLUSTER REPLICATE"
syntax: "CLUSTER REPLICATE master-id"
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
CLUSTER REPLICATE master-id
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Configure this node as a replica. Refuses if the candidate owns slots — `DELSLOTS` first.
