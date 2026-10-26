---
title: "PUBSUB NUMSUB"
description: "Returns how many clients are subscribed to each of the given channels, not counting pattern subscriptions."
version: "1.2"
command: "PUBSUB NUMSUB"
syntax: "PUBSUB NUMSUB [channel ...]"
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
PUBSUB NUMSUB [channel ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many clients are subscribed to each of the given channels, not counting pattern subscriptions.

## Examples

```
> PUBSUB NUMSUB news x
1) "news"
2) (integer) 1
3) "x"
4) (integer) 0
```
