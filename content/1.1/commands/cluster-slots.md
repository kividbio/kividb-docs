---
title: "CLUSTER SLOTS"
description: "Returns which node serves each range of slots: for each range, its first and last slot, then the master as [ip, port, id], then each of its replicas the same way."
version: "1.1"
command: "CLUSTER SLOTS"
syntax: "CLUSTER SLOTS"
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
CLUSTER SLOTS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns which node serves each range of slots: for each range, its first and last slot, then the master as `[ip, port, id]`, then each of its replicas the same way. [`CLUSTER SHARDS`](cluster-shards.md) gives the same with more about each node.

## Examples

```
> CLUSTER SLOTS
1) 1) (integer) 0
   2) (integer) 8191
   3) 1) "127.0.0.1"
      2) (integer) 17641
      3) "b2744aeada9b56dd000f101f31447a33a15c9b08"
   4) 1) "127.0.0.1"
      2) (integer) 17643
      3) "f358de5ffc96bf2cdc0607abd0062224238835b9"
2) 1) (integer) 8192
   2) (integer) 16383
   3) 1) "127.0.0.1"
      2) (integer) 17642
      3) "2e3eefa800e802047f92cb529ac5d1424daebb27"
```
