---
title: "SUNSUBSCRIBE"
description: "Unsubscribes this connection from shard channels, or from all of them if none is given."
version: "1.1"
command: "SUNSUBSCRIBE"
syntax: "SUNSUBSCRIBE [shardchannel ...]"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: ["pubsub"]
acl_categories: ["pubsub", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUNSUBSCRIBE [shardchannel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Unsubscribes this connection from shard channels, or from all of them if none is given.

## Reply

- For each shard channel, an acknowledgement: `sunsubscribe`, the channel, and how many shard subscriptions are left.

## Examples

```
> SUNSUBSCRIBE
1) "sunsubscribe"
2) "orders"
3) (integer) 0
```
