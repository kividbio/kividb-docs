---
title: "CLIENT TRACKING"
description: "Turns client-side caching on or off for this connection."
version: "1.1"
command: "CLIENT TRACKING"
syntax: "CLIENT TRACKING ON|OFF [REDIRECT client-id] [BCAST] [PREFIX prefix [...]] [OPTIN] [OPTOUT] [NOLOOP]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT TRACKING ON|OFF [REDIRECT client-id] [BCAST] [PREFIX prefix [...]] [OPTIN] [OPTOUT] [NOLOOP]
```

**Available since:** 1.1.0
<!-- generated: end -->
Turns client-side caching on or off for this connection. While it is on, the server remembers the keys the connection reads, and tells it when another write changes one of them, so that it can drop that key from its local cache.

A RESP3 connection gets the invalidations as push messages. A RESP2 connection has to `REDIRECT` them to another connection subscribed to `__redis__:invalidate`; without `REDIRECT`, it is sent nothing, as in Redis. Keys written, expired, evicted or flushed are all invalidated.

| Option | Effect |
|---|---|
| `REDIRECT client-id` | Send invalidations to that connection. |
| `BCAST` | Instead of the keys read, invalidate every key starting with the `PREFIX`es given, or every key. |
| `PREFIX prefix ...` | With `BCAST`, the prefixes. |
| `OPTIN` | Remember only reads that follow `CLIENT CACHING yes`. |
| `OPTOUT` | Remember every read but those that follow `CLIENT CACHING no`. |
| `NOLOOP` | Do not tell this connection about its own writes. |

## Examples

```
client 1> HELLO 3
...
client 1> CLIENT TRACKING ON
OK
client 1> GET user:1
"Ada"
client 2> SET user:1 Grace
OK
client 1>
-> invalidate: ["user:1"]
```
