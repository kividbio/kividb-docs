---
title: "PUNSUBSCRIBE"
description: "Unsubscribes this connection from patterns, or from all of them if none is given."
version: "1.2"
command: "PUNSUBSCRIBE"
syntax: "PUNSUBSCRIBE [pattern ...]"
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
PUNSUBSCRIBE [pattern ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@pubsub`, `@slow`
<!-- generated: end -->
Unsubscribes this connection from patterns, or from all of them if none is given.

## Reply

- For each pattern, an acknowledgement: `punsubscribe`, the pattern, and how many subscriptions the connection has left.

## Examples

```
> PUNSUBSCRIBE
1) "punsubscribe"
2) "n*"
3) (integer) 1
```
