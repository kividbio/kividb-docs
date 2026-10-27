---
title: "CLUSTER REPLICAS"
description: "Returns the replicas of the master master-id, each as a CLUSTER NODES line."
version: "1.1"
command: "CLUSTER REPLICAS"
syntax: "CLUSTER REPLICAS master-id"
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
CLUSTER REPLICAS master-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the replicas of the master `master-id`, each as a [`CLUSTER NODES`](cluster-nodes.md) line.

## Known issue

The reply is one bulk string, the lines joined by newlines, where Redis replies with an array of lines. Filed as [kividb#138](https://github.com/kividbio/kividb/issues/138), fixed in 1.2.

## Examples

```
> CLUSTER REPLICAS c8f25b1cf916df71e53ef00653f105b04e6c66aa
"0eacc11dc2a8cdbeca2028d952a58ae4485dcd27 127.0.0.1:17633@27633 slave c8f25b1cf916df71e53ef00653f105b04e6c66aa 1792968858779 1792968858799 1 connected\n"
```
