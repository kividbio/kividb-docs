---
title: "CLUSTER LINKS"
description: "Returns this node's links to other nodes on the cluster bus: for each, direction, node, create-time, events, send-buffer-allocated and send-buffer-used."
version: "1.1"
command: "CLUSTER LINKS"
syntax: "CLUSTER LINKS"
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
CLUSTER LINKS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this node's links to other nodes on the cluster bus: for each, `direction`, `node`, `create-time`, `events`, `send-buffer-allocated` and `send-buffer-used`.

## Examples

```
> CLUSTER LINKS
1)  1) "direction"
    2) "to"
    3) "node"
    4) "f358de5ffc96bf2cdc0607abd0062224238835b9"
    5) "create-time"
    6) (integer) 1792969096455
    7) "events"
    8) "rw"
    9) "send-buffer-allocated"
   10) (integer) 0
   11) "send-buffer-used"
   12) (integer) 0
2) ...
```
