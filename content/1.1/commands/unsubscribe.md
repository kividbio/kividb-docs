---
title: "UNSUBSCRIBE"
description: "Unsubscribe from channels."
version: "1.1"
command: "UNSUBSCRIBE"
syntax: "UNSUBSCRIBE [channel ...]"
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
UNSUBSCRIBE [channel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Unsubscribe from channels. With no arguments, unsubscribes from all channels. Each unsubscription sends an ack: `["unsubscribe", channel, remaining_count]`
