---
title: "CLUSTER SLOTS"
description: "Slot-to-node mapping."
version: "1.2"
command: "CLUSTER SLOTS"
syntax: "CLUSTER SLOTS"
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
CLUSTER SLOTS
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Slot-to-node mapping. Each entry: `[start, end, [master_ip, port, id], ...replicas]`.
