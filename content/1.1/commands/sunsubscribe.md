---
title: "SUNSUBSCRIBE"
description: "Unsubscribe from shard channels."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
SUNSUBSCRIBE [shardchannel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Unsubscribe from shard channels. With no arguments, unsubscribes from all shard channels
