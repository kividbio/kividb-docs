---
title: "PUBLISH"
description: "Sends message to every client subscribed to channel, with SUBSCRIBE, or to a pattern that matches it, with PSUBSCRIBE."
version: "1.2"
command: "PUBLISH"
syntax: "PUBLISH channel message"
group: "pub-sub"
since: "1.1.0"
arity: 3
flags: ["fast", "pubsub"]
acl_categories: ["fast", "pubsub"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PUBLISH channel message
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@pubsub`
<!-- generated: end -->
Sends `message` to every client subscribed to `channel`, with [`SUBSCRIBE`](subscribe.md), or to a pattern that matches it, with [`PSUBSCRIBE`](psubscribe.md). Messages are not stored: a client that is not subscribed when one is sent never gets it.

## Reply

- The number of clients that got the message. A client subscribed both to the channel and to a matching pattern gets it, and is counted, twice.

## Examples

```
client 1> SUBSCRIBE news
1) "subscribe"
2) "news"
3) (integer) 1
client 2> PUBLISH news hello
(integer) 1
client 1>
1) "message"
2) "news"
3) "hello"
```
