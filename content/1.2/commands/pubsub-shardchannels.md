---
title: "PUBSUB SHARDCHANNELS"
description: "Returns the shard channels with at least one subscriber, or those matching a glob-style pattern."
version: "1.2"
command: "PUBSUB SHARDCHANNELS"
syntax: "PUBSUB SHARDCHANNELS [pattern]"
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
PUBSUB SHARDCHANNELS [pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the shard channels that at least one client is subscribed to with [`SSUBSCRIBE`](ssubscribe.md), sorted. With `pattern`, only those whose names match it, with the glob syntax of [`PSUBSCRIBE`](psubscribe.md): `*`, `?`, `[abc]`. Ordinary channels are not listed; [`PUBSUB CHANNELS`](pubsub-channels.md) lists those.

In a cluster, shard channels are placed in slots like keys, and a client subscribes on the node that owns the slot or one of its replicas. Each node lists only its own subscribers' channels, so to see all of them, ask every node. See [Pub/Sub in a cluster](../guides/pub-sub.md#in-a-cluster).

## Reply

- An array of shard channel names; an empty array if there are none.

## Examples

```
client 2> SSUBSCRIBE orders
...
client 3> SSUBSCRIBE invoices
...
client 1> PUBSUB SHARDCHANNELS
1) "invoices"
2) "orders"
client 1> PUBSUB SHARDCHANNELS o*
1) "orders"
```
