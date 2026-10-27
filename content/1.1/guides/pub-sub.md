---
title: "Pub/Sub and keyspace notifications"
description: "Send messages to subscribers with PUBLISH and SUBSCRIBE, in a cluster with sharded channels, and be told of changes to keys."
version: "1.1"
weight: 40
---

## Pub/Sub

A client that [`SUBSCRIBE`](../commands/subscribe.md)s to a channel receives every message [`PUBLISH`](../commands/publish.md)ed to it from then on. [`PSUBSCRIBE`](../commands/psubscribe.md) subscribes to every channel matching a pattern: `*`, `?`, `[abc]`, `[^abc]`, `[a-z]`, and `\` before a character to match it as itself.

```
subscriber> SUBSCRIBE orders
1) "subscribe"
2) "orders"
3) (integer) 1

publisher> PUBLISH orders "order:9001 paid"
(integer) 1

subscriber>
1) "message"
2) "orders"
3) "order:9001 paid"
```

`PUBLISH` replies with how many subscriptions received the message. A connection using RESP2 can send only subscription commands, `PING`, `QUIT` and `RESET` while it is subscribed; one using RESP3 can send anything, and receives messages as push frames.

### Delivery

A message reaches the clients subscribed when it is published, at most once: it is not stored, so a client that is not connected, or not yet subscribed, never gets it. For lasting messages that a consumer can come back to, use a [stream](../commands/xadd.md). Messages arrive in the order they were published.

A subscriber that does not read its messages is disconnected once 32 MB of them wait for it, or more than 8 MB for 60 seconds, with a line in the log. The limits cannot be changed.

On a standalone master, messages also reach its replicas' subscribers.

### In a cluster

`PUBLISH` sends the message to every node, and each delivers it to its own subscribers: a client may subscribe on any node. Every message crosses the cluster bus to every node.

Sharded channels, [`SSUBSCRIBE`](../commands/ssubscribe.md) and [`SPUBLISH`](../commands/spublish.md), are placed in slots like keys: a message goes to the node that owns the channel's slot, and its replicas, only. `SPUBLISH` to another node answers `MOVED`. Use them for many channels, or busy ones, in a large cluster.

### Known issues

Filed as [kividb#161](https://github.com/kividbio/kividb/issues/161), fixed in 1.2:

- A channel name must be valid UTF-8: `PUBLISH` refuses one that is not.
- `SSUBSCRIBE` is not redirected: on a node that does not own the channel's slot, it succeeds and receives nothing. Subscribe on the owner, or a replica of it.

## Keyspace notifications

With [`notify-keyspace-events`](../reference/configuration.md#notify-keyspace-events) set, the server publishes a message for changes to keys: on `__keyspace@<db>__:<key>`, whose message is the event, and on `__keyevent@<db>__:<event>`, whose message is the key.

```
> CONFIG SET notify-keyspace-events KEA
OK
> PSUBSCRIBE __keyevent@0__:*
...
other> SET user:1 Ada
OK
1) "pmessage"
2) "__keyevent@0__:*"
3) "__keyevent@0__:set"
4) "user:1"
```

| Letter | Events |
|---|---|
| `K`, `E` | Publish on the keyspace channels, the keyevent channels. One of them is needed. |
| `g` | Generic: `del`, `expire`, `persist`, `rename_from`, `rename_to`, `copy_to`, `restore`. |
| `$`, `l`, `s`, `h`, `z`, `t` | Strings, lists, sets, hashes, sorted sets, streams. |
| `a` | Arrays. |
| `x` | `expired`: a key whose time to live passed was deleted. |
| `e` | `evicted`: a key deleted at the memory limit. |
| `n` | `new`: a key was created. |
| `A` | All of `g$lshzxeta`. |

`expired` is published when the key is deleted, which can be after its time to live has passed: when it is next read, or when the background task, which runs ten times a second, finds it. Notifications are not stored, like any message, and in a cluster each node publishes those of its own keys, to its own subscribers.

### Known issues

Filed as [kividb#160](https://github.com/kividbio/kividb/issues/160), fixed in 1.2:

- Some events have other names than Redis's: `INCR`, `DECR` and `DECRBY` publish `incr`, `decr`, `decrby` (Redis: `incrby`); `GETDEL` publishes `getdel` (Redis: `del`); `GETSET` and `SETNX` publish `getset` and `setnx` (Redis: `set`); `GETEX` publishes `getex`; `LMOVE` publishes `lmove` on both keys.
- `SETRANGE`, `SETBIT`, `BITOP`, `BITFIELD`, `PFADD`, `PFMERGE`, `GEOADD`, `MOVE`, `SWAPDB` and the JSON, time series and vector set commands publish nothing.
- `m`, key misses, is accepted and never publishes.
