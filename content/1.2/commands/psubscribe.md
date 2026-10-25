---
title: "PSUBSCRIBE"
description: "Subscribes this connection to every channel matching a glob-style pattern."
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PSUBSCRIBE pattern [pattern ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Subscribes this connection to every channel matching a glob-style pattern. A message to a matching channel arrives as a four-element array: `pmessage`, the pattern, the channel it was sent to, the message.

## Reply

- For each pattern, an acknowledgement: `psubscribe`, the pattern, and how many subscriptions the connection now has.

## Examples

```
> PSUBSCRIBE n*
1) "psubscribe"
2) "n*"
3) (integer) 1
```

After another client's `PUBLISH news hello`:

```
1) "pmessage"
2) "n*"
3) "news"
4) "hello"
```
