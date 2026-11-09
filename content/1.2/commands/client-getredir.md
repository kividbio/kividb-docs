---
title: "CLIENT GETREDIR"
description: "Returns the ID of the connection this one's client-side caching invalidations go to, as set with REDIRECT in CLIENT TRACKING."
version: "1.2"
command: "CLIENT GETREDIR"
syntax: "CLIENT GETREDIR"
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
CLIENT GETREDIR
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the ID of the connection this one's [client-side caching](../guides/client-side-caching.md) invalidations go to, as set with `REDIRECT` in [`CLIENT TRACKING`](client-tracking.md).

A RESP2 connection cannot receive invalidations alongside its replies, so a client library tracks keys on one connection and subscribes a second one to `__redis__:invalidate`; this tells it which connection that is. [`CLIENT TRACKINGINFO`](client-trackinginfo.md) reports the same ID with the rest of the tracking state.

## Reply

- `-1`: tracking is off.
- `0`: tracking is on, and invalidations come to this connection itself.
- Otherwise, the ID of the connection they go to.

## Examples

```
> CLIENT GETREDIR
(integer) -1
> CLIENT TRACKING ON BCAST PREFIX user:
OK
> CLIENT GETREDIR
(integer) 0
```
