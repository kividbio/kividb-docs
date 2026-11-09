---
title: "PUBSUB NUMSUB"
description: "Returns, for each channel named, how many clients are subscribed to it with SUBSCRIBE."
version: "1.2"
command: "PUBSUB NUMSUB"
syntax: "PUBSUB NUMSUB [channel ...]"
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
PUBSUB NUMSUB [channel ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns, for each channel named, how many clients are subscribed to it with [`SUBSCRIBE`](subscribe.md). Clients that would receive its messages through a pattern subscription ([`PSUBSCRIBE`](psubscribe.md)) are not counted, so the figure can be lower than what [`PUBLISH`](publish.md) replies. A channel no one is subscribed to gets `0`. Shard channels have [`PUBSUB SHARDNUMSUB`](pubsub-shardnumsub.md).

The channels come back in the order given. Without any channel, the reply is an empty array. Counts are this server's subscribers only; in a cluster, each node answers for its own clients.

## Reply

- A flat array of channel, count pairs.

## Examples

```
client 2> SUBSCRIBE news sport
...
client 3> SUBSCRIBE news
...
client 4> PSUBSCRIBE n*
...
client 1> PUBSUB NUMSUB news sport x
1) "news"
2) (integer) 2
3) "sport"
4) (integer) 1
5) "x"
6) (integer) 0
client 1> PUBLISH news hi
(integer) 3
```
