---
title: "PUBLISH"
description: "Post a message to a channel."
version: "1.1"
command: "PUBLISH"
syntax: "PUBLISH channel message"
group: "pub-sub"
since: "1.1.0"
arity: 3
flags: ["fast", "pubsub"]
acl_categories: ["fast", "pubsub"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PUBLISH channel message
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@pubsub`
<!-- generated: end -->
## Description

Post a message to a channel. Delivered to all `SUBSCRIBE` subscribers and all `PSUBSCRIBE` subscribers whose pattern matches the channel. Returns the total number of clients that received the message
