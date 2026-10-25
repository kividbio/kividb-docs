---
title: "CLUSTER FORGET"
description: "Removes the node node-id from this node's table."
version: "1.2"
command: "CLUSTER FORGET"
syntax: "CLUSTER FORGET node-id"
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
CLUSTER FORGET node-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Removes the node `node-id` from this node's table. Slots it owned become unassigned. For 60 seconds this node does not take it back from other nodes' gossip, so it has time to be forgotten on every node.

## Reply

- `OK`.
- `ERR Unknown node`.
- `ERR I tried hard but I can't forget myself...`.

## Examples

```
> CLUSTER FORGET 0eacc11dc2a8cdbeca2028d952a58ae4485dcd27
OK
```
