---
title: "PUBSUB SHARDCHANNELS"
description: "Returns the shard channels with at least one subscriber, or those matching a glob-style pattern."
version: "1.2"
command: "PUBSUB SHARDCHANNELS"
syntax: "PUBSUB SHARDCHANNELS [pattern]"
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
PUBSUB SHARDCHANNELS [pattern]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the shard channels with at least one subscriber, or those matching a glob-style pattern.

## Examples

```
> PUBSUB SHARDCHANNELS
1) "orders"
```
