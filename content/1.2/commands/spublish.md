---
title: "SPUBLISH"
description: "Sends message to the clients subscribed to the shard channel shardchannel with SSUBSCRIBE."
version: "1.2"
command: "SPUBLISH"
syntax: "SPUBLISH shardchannel message"
group: "pub-sub"
since: "1.1.0"
arity: 3
flags: ["fast", "pubsub", "readonly"]
acl_categories: ["fast", "pubsub"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SPUBLISH shardchannel message
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@pubsub`
<!-- generated: end -->
Sends `message` to the clients subscribed to the shard channel `shardchannel` with [`SSUBSCRIBE`](ssubscribe.md). Shard channels are separate from ordinary ones: `PUBLISH` does not reach shard subscribers, and patterns do not match shard channels.

## Reply

- The number of clients that got the message.

## Examples

```
client 1> SSUBSCRIBE orders
1) "ssubscribe"
2) "orders"
3) (integer) 1
client 2> SPUBLISH orders o1
(integer) 1
client 2> PUBLISH orders x
(integer) 0
client 1>
1) "smessage"
2) "orders"
3) "o1"
```
