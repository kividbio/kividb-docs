---
title: "CLUSTER MYSHARDID"
description: "Returns the ID of this node's shard: a master's own ID, or a replica's master's."
version: "1.2"
command: "CLUSTER MYSHARDID"
syntax: "CLUSTER MYSHARDID"
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
CLUSTER MYSHARDID
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the ID of this node's shard: a master's own ID, or a replica's master's.

## Examples

```
> CLUSTER MYSHARDID
"b2744aeada9b56dd000f101f31447a33a15c9b08"
```
