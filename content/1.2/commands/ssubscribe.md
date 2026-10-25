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
Subscribes this connection to shard channels. A message arrives as `smessage`, the shard channel, the message. See [`SPUBLISH`](spublish.md).

## Reply

- For each shard channel, an acknowledgement: `ssubscribe`, the channel, and the count of shard subscriptions.
