---
title: "SUBSCRIBE"
description: "Subscribes this connection to channels."
version: "1.1"
command: "SUBSCRIBE"
syntax: "SUBSCRIBE channel [channel ...]"
group: "pub-sub"
since: "1.1.0"
arity: -2
flags: ["pubsub"]
acl_categories: ["pubsub", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUBSCRIBE channel [channel ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Subscribes this connection to channels. Each message [`PUBLISH`](publish.md)ed to one of them then arrives as a three-element array: `message`, the channel, the message.

A subscribed connection speaking RESP2 can only send `SUBSCRIBE`, `PSUBSCRIBE`, `SSUBSCRIBE`, their `UNSUBSCRIBE` commands, `PING`, `QUIT` and `RESET` until it unsubscribes from everything. One speaking RESP3 (after `HELLO 3`) can send any command, and messages arrive as push replies between the replies to its commands. Subscribing twice to a channel delivers its messages once.

## Reply

- For each channel, an acknowledgement: `subscribe`, the channel, and how many subscriptions the connection now has.

## Examples

```
> SUBSCRIBE news sport
1) "subscribe"
2) "news"
3) (integer) 1
1) "subscribe"
2) "sport"
3) (integer) 2
> GET k
(error) ERR Can't execute 'get': only (P|S)SUBSCRIBE / (P|S)UNSUBSCRIBE / PING / QUIT / RESET are allowed in this context
```
