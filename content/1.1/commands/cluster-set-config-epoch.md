---
title: "CLUSTER SET-CONFIG-EPOCH"
description: "Sets this node's config epoch, for giving each node of a new cluster a different one before it serves."
version: "1.1"
command: "CLUSTER SET-CONFIG-EPOCH"
syntax: "CLUSTER SET-CONFIG-EPOCH epoch"
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
CLUSTER SET-CONFIG-EPOCH epoch
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets this node's config epoch, for giving each node of a new cluster a different one before it serves. It is refused once the epoch is not `0`.

## Reply

- `OK`.
- `ERR Node config epoch is already non-zero`.
