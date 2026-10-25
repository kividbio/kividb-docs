---
title: "SPUBLISH"
description: "Post a message to a shard channel."
version: "1.1"
command: "SPUBLISH"
syntax: "SPUBLISH shardchannel message"
group: "pub-sub"
since: "1.1.0"
arity: 3
flags: ["fast", "pubsub", "readonly"]
acl_categories: ["fast", "pubsub"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SPUBLISH shardchannel message
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@pubsub`
<!-- generated: end -->
## Description

Post a message to a shard channel. Delivered only to `SSUBSCRIBE` subscribers — does not match patterns or regular subscriptions. Returns the number of shard subscribers that received it
