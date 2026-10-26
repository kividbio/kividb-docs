---
title: "PUBSUB SHARDNUMSUB"
description: "Returns how many clients are subscribed to each of the given shard channels."
version: "1.2"
command: "PUBSUB SHARDNUMSUB"
syntax: "PUBSUB SHARDNUMSUB [shardchannel ...]"
group: "pub-sub"
since: "1.1.0"
history: []
container: "PUBSUB"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PUBSUB SHARDNUMSUB [shardchannel ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many clients are subscribed to each of the given shard channels.

## Examples

```
> PUBSUB SHARDNUMSUB orders
1) "orders"
2) (integer) 1
```
