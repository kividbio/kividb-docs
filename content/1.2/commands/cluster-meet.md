---
title: "CLUSTER MEET"
description: "Introduces the node at ip port to this one, which then tells the rest of the cluster about it."
version: "1.2"
command: "CLUSTER MEET"
syntax: "CLUSTER MEET ip port [cluster-bus-port]"
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
CLUSTER MEET ip port [cluster-bus-port]
```

**Available since:** 1.1.0
<!-- generated: end -->
Introduces the node at `ip port` to this one, which then tells the rest of the cluster about it. The bus port defaults to `port + 10000`. The handshake runs in the background: the reply is `OK` before it is done, and a node that cannot be reached is not added.

## Examples

```
> CLUSTER MEET 127.0.0.1 17642
OK
```
