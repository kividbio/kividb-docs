---
title: "CLUSTER MYID"
description: "Returns this node's ID: 40 hexadecimal characters, kept in nodes.conf across restarts."
version: "1.1"
command: "CLUSTER MYID"
syntax: "CLUSTER MYID"
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
CLUSTER MYID
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this node's ID: 40 hexadecimal characters, kept in `nodes.conf` across restarts. [`CLUSTER RESET HARD`](cluster-reset.md) gives the node a new one.

## Examples

```
> CLUSTER MYID
"b2744aeada9b56dd000f101f31447a33a15c9b08"
```
