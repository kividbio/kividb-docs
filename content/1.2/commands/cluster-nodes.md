---
title: "CLUSTER NODES"
description: "Returns the node table, one line per node, in the format of Redis's CLUSTER NODES: ID, ip:port@bus-port, flags (myself, master, slave, fail?, fail, …), the master's ID for a replica or -, the times t…"
version: "1.2"
command: "CLUSTER NODES"
syntax: "CLUSTER NODES"
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
CLUSTER NODES
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the node table, one line per node, in the format of Redis's `CLUSTER NODES`: ID, `ip:port@bus-port`, flags (`myself`, `master`, `slave`, `fail?`, `fail`, …), the master's ID for a replica or `-`, the times the last ping was sent and the last pong received, the config epoch, the link state, and the slots it serves.

## Examples

```
> CLUSTER NODES
2e3eefa800e802047f92cb529ac5d1424daebb27 127.0.0.1:17642@27642 master - 1792969096459 1792969096486 0 connected 8192-16383
b2744aeada9b56dd000f101f31447a33a15c9b08 127.0.0.1:17641@27641 myself,master - 0 0 1 connected 0-8191
f358de5ffc96bf2cdc0607abd0062224238835b9 127.0.0.1:17643@27643 slave b2744aeada9b56dd000f101f31447a33a15c9b08 1792969096455 1792969096481 0 connected
```
