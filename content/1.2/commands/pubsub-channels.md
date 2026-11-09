---
title: "PUBSUB CHANNELS"
description: "Returns the channels that at least one client is subscribed to with SUBSCRIBE, sorted."
version: "1.2"
command: "PUBSUB CHANNELS"
syntax: "PUBSUB CHANNELS [pattern]"
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
PUBSUB CHANNELS [pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the channels that at least one client is subscribed to with [`SUBSCRIBE`](subscribe.md), sorted. With `pattern`, only those whose names match it, with the glob syntax of [`PSUBSCRIBE`](psubscribe.md): `*`, `?`, `[abc]`. Use it to see what is being listened to, for example while debugging a publisher whose messages reach no one.

Pattern subscriptions are not channels and are not listed, nor are shard channels; [`PUBSUB NUMPAT`](pubsub-numpat.md) and [`PUBSUB SHARDCHANNELS`](pubsub-shardchannels.md) cover those. The list is this server's subscribers only: in a cluster, each node answers for the clients connected to it. See [Pub/Sub](../guides/pub-sub.md).

## Reply

- An array of channel names; an empty array if there are none.

## Examples

```
client 2> SUBSCRIBE news sport
...
client 3> PSUBSCRIBE n*
...
client 1> PUBSUB CHANNELS
1) "news"
2) "sport"
client 1> PUBSUB CHANNELS s*
1) "sport"
client 1> PUBSUB CHANNELS x*
(empty array)
```
