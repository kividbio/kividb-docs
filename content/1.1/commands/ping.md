---
title: "PING"
description: "In subscriber mode returns [\"pong\", message] (a 2-element array), not +PONG."
version: "1.1"
command: "PING"
syntax: "PING [message]"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
PING [message]
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
## Description

In subscriber mode returns `["pong", message]` (a 2-element array), not `+PONG`. This is the standard Redis subscriber-mode PING behaviour

With no argument returns `PONG`. With a message returns that message as a **bulk string** (Redis echo semantics). Subscriber mode still uses the Pub/Sub array reply
