---
title: "SSUBSCRIBE"
description: "Subscribes this connection to shard channels."
version: "1.2"
command: "SSUBSCRIBE"
syntax: "SSUBSCRIBE shardchannel [shardchannel ...]"
group: "pub-sub"
since: "1.1.0"
arity: -2
flags: ["pubsub"]
acl_categories: ["pubsub", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SSUBSCRIBE shardchannel [shardchannel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Subscribes this connection to shard channels. Each message [`SPUBLISH`](spublish.md)ed to one of them then arrives as a three-element array: `smessage`, the shard channel, the message. Shard channels are separate from ordinary ones: [`PUBLISH`](publish.md) does not reach them, and pattern subscriptions do not match them.

In a cluster, a shard channel is placed in a slot as a key is, and its messages go only to the node that owns the slot and its replicas, not across the whole cluster. All the channels of one `SSUBSCRIBE` must be in the same slot, or the reply is `CROSSSLOT`; a hash tag, `{orders}.eu`, puts several in one. On a node that is neither the slot's owner nor one of its replicas, the reply is `MOVED`. On a standalone server, any channels can be subscribed together. See [Pub/Sub in a cluster](../guides/pub-sub.md#in-a-cluster).

While subscribed, a connection speaking RESP2 can only send subscription commands, `PING`, `QUIT` and `RESET`, as after [`SUBSCRIBE`](subscribe.md). [`SUNSUBSCRIBE`](sunsubscribe.md) ends shard subscriptions.

## Reply

- For each shard channel, an acknowledgement: `ssubscribe`, the channel, and how many subscriptions the connection now has.

The count is of the connection's shard channels only, as in Redis; that after `SUBSCRIBE` or `PSUBSCRIBE` counts channels and patterns. Before 1.2.1 every count was of all three together, so the numbers differed from Redis's for a connection that mixed them.

## Examples

On a cluster node that owns every slot:

```
> SSUBSCRIBE orders invoices
(error) CROSSSLOT Keys in request don't hash to the same slot
> SSUBSCRIBE {orders}.eu {orders}.us
1) "ssubscribe"
2) "{orders}.eu"
3) (integer) 1
1) "ssubscribe"
2) "{orders}.us"
3) (integer) 2
> SUBSCRIBE news
1) "subscribe"
2) "news"
3) (integer) 3
```

```
client 2> SPUBLISH {orders}.eu o1
(integer) 1
client 1>
1) "smessage"
2) "{orders}.eu"
3) "o1"
```
