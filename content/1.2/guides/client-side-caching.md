---
title: "Client-side caching"
description: "Let clients keep values in their own memory, and be told by the server when one changes: CLIENT TRACKING, its modes, and its limits."
version: "1.2"
weight: 50
---

A client that keeps the values it read in its own memory answers the next read without a round trip. The server tells it when a value it holds changes, so that it drops it: that is [`CLIENT TRACKING`](../commands/client-tracking.md), as in Redis 6 and later. Client libraries do it for you (`redis-py`'s client-side cache, Lettuce's `ClientSideCaching`, `rueidis`).

## How it works

With RESP3, on the same connection:

```
> HELLO 3
...
> CLIENT TRACKING ON
OK
> GET user:1
"Ada"
```

The server remembers that this client read `user:1`. When any client changes it, deletes it, or it expires or is evicted, the server sends the reader:

```
>2
1) "invalidate"
2) 1) "user:1"
```

and forgets that it read it, until it reads it again. `FLUSHALL` and `FLUSHDB` send an invalidation of everything, with nil in place of the keys.

With RESP2, invalidations go to another connection: one subscribed to `__redis__:invalidate`, whose ID is given with `REDIRECT`:

```
conn 2> CLIENT ID
(integer) 8
conn 2> SUBSCRIBE __redis__:invalidate
conn 1> CLIENT TRACKING ON REDIRECT 8
OK
```

## Modes

| Option | Effect |
|---|---|
| (none) | The server remembers each key the client reads, and tells it of those. |
| `BCAST` `PREFIX p ...` | The server remembers nothing: the client is told of every change to a key under the prefixes, whether it read it or not. Costs the server no memory; costs the client messages. |
| `OPTIN` | Only reads after `CLIENT CACHING yes` are remembered: for clients that cache some keys. |
| `OPTOUT` | Every read but those after `CLIENT CACHING no`. |
| `NOLOOP` | The client is not told of its own changes. |

## Limits

The server remembers at most [`tracking-table-max-keys`](../reference/configuration.md#tracking-table-max-keys) keys (a million) for all clients together. Beyond it, it drops some, and tells their readers to drop them, as if they had changed. `INFO clients` gives `tracking_total_keys`.

A client must read the invalidations it is sent: a value is stale in its cache from the moment it changes until the invalidation is read.

A connection has room for 65536 messages waiting to be sent to it, invalidations among them. A client that falls further behind than that is closed, with a line in the server's log, so that it drops what it cached rather than serve values that have changed:

```
2026-10-27T15:23:06.442Z 18008 [WARN] Client id=19 closed: it uses client-side caching and did not read its invalidation messages, over 65536 waiting
```

Before 1.2, a connection had room for 512 (256 with io_uring), and the invalidations beyond were dropped: the client kept serving stale values without being told.
