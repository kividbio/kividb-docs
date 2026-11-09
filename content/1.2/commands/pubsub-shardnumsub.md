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
Returns, for each shard channel named, how many clients are subscribed to it with [`SSUBSCRIBE`](ssubscribe.md). A shard channel no one is subscribed to gets `0`, and so does an ordinary channel's name: subscriptions made with [`SUBSCRIBE`](subscribe.md) are counted by [`PUBSUB NUMSUB`](pubsub-numsub.md) instead.

The channels come back in the order given; without any, the reply is an empty array. In a cluster, each node counts only its own clients, so ask the node that owns the channel's slot, and its replicas. See [Pub/Sub in a cluster](../guides/pub-sub.md#in-a-cluster).

## Reply

- A flat array of shard channel, count pairs.

## Examples

```
client 2> SSUBSCRIBE orders
...
client 3> SUBSCRIBE news
...
client 1> PUBSUB SHARDNUMSUB orders news
1) "orders"
2) (integer) 1
3) "news"
4) (integer) 0
```
