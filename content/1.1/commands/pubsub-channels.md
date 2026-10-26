---
title: "PUBSUB CHANNELS"
description: "Returns the channels with at least one subscriber, or those matching a glob-style pattern."
version: "1.1"
command: "PUBSUB CHANNELS"
syntax: "PUBSUB CHANNELS [pattern]"
group: "pub-sub"
since: "1.1.0"
history: []
container: "PUBSUB"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PUBSUB CHANNELS [pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the channels with at least one subscriber, or those matching a glob-style pattern. Pattern subscriptions are not counted.

## Examples

```
> PUBSUB CHANNELS
1) "news"
2) "sport"
> PUBSUB CHANNELS s*
1) "sport"
```
