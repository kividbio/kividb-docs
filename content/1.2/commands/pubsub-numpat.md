---
title: "PUBSUB NUMPAT"
description: "Returns how many pattern subscriptions there are, from all clients together."
version: "1.2"
command: "PUBSUB NUMPAT"
syntax: "PUBSUB NUMPAT"
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
PUBSUB NUMPAT
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many distinct patterns clients are subscribed to with [`PSUBSCRIBE`](psubscribe.md). A pattern that several clients subscribe to counts once, as in Redis since 7.0; to see how many subscriptions one connection has, look at the `psub=` field of [`CLIENT LIST`](client-list.md).

Use it as a cheap check on pattern subscriptions, which cost more than channel subscriptions: every published message is matched against every pattern. It counts this server's subscribers only; in a cluster each node answers for its own clients. See [Pub/Sub](../guides/pub-sub.md).

## Reply

- The number of patterns; `0` if there are none.

## Examples

```
client 2> PSUBSCRIBE n* s*
...
client 3> PSUBSCRIBE n*
...
client 1> PUBSUB NUMPAT
(integer) 2
```
