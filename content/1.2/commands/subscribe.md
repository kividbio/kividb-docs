---
title: "SUBSCRIBE"
description: "Subscribe to one or more channels."
version: "1.2"
command: "SUBSCRIBE"
syntax: "SUBSCRIBE channel [channel ...]"
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
SUBSCRIBE channel [channel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Subscribe to one or more channels. Each subscription sends an ack: `["subscribe", channel, total_count]`. Idempotent — subscribing to a channel you are already subscribed to does not create duplicate deliveries
