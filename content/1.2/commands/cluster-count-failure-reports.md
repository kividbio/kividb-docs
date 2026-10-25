---
title: "CLUSTER COUNT-FAILURE-REPORTS"
description: "Number of distinct nodes currently flagging this node as failing."
version: "1.2"
command: "CLUSTER COUNT-FAILURE-REPORTS"
syntax: "CLUSTER COUNT-FAILURE-REPORTS node-id"
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
CLUSTER COUNT-FAILURE-REPORTS node-id
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Number of distinct nodes currently flagging this node as failing. Excludes the local node's own opinion.
