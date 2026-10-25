---
title: "CLUSTER BUMPEPOCH"
description: "Increments the cluster's current epoch and gives it to this node, so that this node's claims to its slots win over older ones."
version: "1.2"
command: "CLUSTER BUMPEPOCH"
syntax: "CLUSTER BUMPEPOCH"
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
CLUSTER BUMPEPOCH
```

**Available since:** 1.1.0
<!-- generated: end -->
Increments the cluster's current epoch and gives it to this node, so that this node's claims to its slots win over older ones. Returns `BUMPED` and the new epoch.

## Examples

```
> CLUSTER BUMPEPOCH
BUMPED 2
```
