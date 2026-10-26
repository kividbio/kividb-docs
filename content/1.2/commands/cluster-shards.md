---
title: "CLUSTER SHARDS"
description: "Returns each shard: its slot ranges, and its nodes, each with id, port, ip, endpoint, role (master or replica), replication-offset and health."
version: "1.2"
command: "CLUSTER SHARDS"
syntax: "CLUSTER SHARDS"
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
CLUSTER SHARDS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns each shard: its slot ranges, and its nodes, each with `id`, `port`, `ip`, `endpoint`, `role` (`master` or `replica`), `replication-offset` and `health`.

## Examples

```
> CLUSTER SHARDS
1) 1) "slots"
   2) 1) (integer) 0
      2) (integer) 8191
   3) "nodes"
   4) 1)  1) "id"
          2) "b2744aeada9b56dd000f101f31447a33a15c9b08"
          3) "port"
          4) (integer) 17641
          5) "ip"
          6) "127.0.0.1"
          7) "endpoint"
          8) "127.0.0.1"
          9) "role"
         10) "master"
         11) "replication-offset"
         12) (integer) 0
         13) "health"
         14) "online"
      2) ...
2) ...
```
