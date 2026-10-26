---
title: "CLUSTER COUNT-FAILURE-REPORTS"
description: "Returns how many other nodes currently report node-id as failing."
version: "1.2"
command: "CLUSTER COUNT-FAILURE-REPORTS"
syntax: "CLUSTER COUNT-FAILURE-REPORTS node-id"
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
CLUSTER COUNT-FAILURE-REPORTS node-id
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many other nodes currently report `node-id` as failing. When a majority of masters do, the node is marked `FAIL` and a replica takes its place.

## Examples

```
> CLUSTER COUNT-FAILURE-REPORTS 2e3eefa800e802047f92cb529ac5d1424daebb27
(integer) 0
```
