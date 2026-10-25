---
title: "UNSUBSCRIBE"
description: "Unsubscribes this connection from channels, or from all of them if none is given."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
UNSUBSCRIBE [channel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Unsubscribes this connection from channels, or from all of them if none is given.

## Reply

- For each channel, an acknowledgement: `unsubscribe`, the channel, and how many subscriptions the connection has left. At `0`, the connection can send any command again.

## Examples

```
> UNSUBSCRIBE news
1) "unsubscribe"
2) "news"
3) (integer) 2
```
