---
title: "PSUBSCRIBE"
description: "Subscribe to all channels matching a glob pattern."
version: "1.2"
command: "PSUBSCRIBE"
syntax: "PSUBSCRIBE pattern [pattern ...]"
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
PSUBSCRIBE pattern [pattern ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Subscribe to all channels matching a glob pattern. Messages are delivered as `["pmessage", pattern, channel, payload]` — note the 4-element format vs the 3-element `message` format
