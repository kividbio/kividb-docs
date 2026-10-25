---
title: "SSUBSCRIBE"
description: "Subscribe to one or more shard channels."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SSUBSCRIBE shardchannel [shardchannel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Subscribe to one or more shard channels. Messages are delivered as `["smessage", shardchannel, payload]`
