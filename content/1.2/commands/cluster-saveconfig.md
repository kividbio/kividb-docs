---
title: "CLUSTER SAVECONFIG"
description: "Writes the node's topology to nodes.conf (cluster-config-file) now."
version: "1.2"
command: "CLUSTER SAVECONFIG"
syntax: "CLUSTER SAVECONFIG"
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
CLUSTER SAVECONFIG
```

**Available since:** 1.1.0
<!-- generated: end -->
Writes the node's topology to `nodes.conf` (`cluster-config-file`) now. The node writes it itself whenever the topology changes.

## Examples

```
> CLUSTER SAVECONFIG
OK
```
