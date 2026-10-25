---
title: "CLUSTER RESET"
description: "Clear topology: forget the other nodes and the slot assignments."
version: "1.2"
command: "CLUSTER RESET"
syntax: "CLUSTER RESET [HARD | SOFT]"
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
CLUSTER RESET [HARD | SOFT]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Clear topology: forget the other nodes and the slot assignments. `SOFT` (default) keeps the node ID and epochs, and is refused on a master that holds keys; `HARD` also resets the epochs, flushes the dataset and gives the node a new ID.
