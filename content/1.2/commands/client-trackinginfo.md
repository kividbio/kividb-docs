---
title: "CLIENT TRACKINGINFO"
description: "Returns this connection's client-side caching state, as set with CLIENT TRACKING."
version: "1.2"
command: "CLIENT TRACKINGINFO"
syntax: "CLIENT TRACKINGINFO"
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
CLIENT TRACKINGINFO
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this connection's [client-side caching](../guides/client-side-caching.md) state, as set with [`CLIENT TRACKING`](client-tracking.md). Client libraries use it to check that tracking is set up as they asked.

The reply is three name-value pairs:

- `flags`: `off`, or `on` with any of `bcast`, `optin`, `optout`, `noloop`, and `caching-yes` or `caching-no` while an [`CLIENT CACHING`](client-caching.md) choice is pending for the next command.
- `redirect`: `-1` when tracking is off, `0` when invalidations come to this connection, or the ID of the connection they go to.
- `prefixes`: the prefixes given in broadcast mode.

## Examples

```
> CLIENT TRACKINGINFO
1) "flags"
2) 1) "off"
3) "redirect"
4) (integer) -1
5) "prefixes"
6) (empty array)
> CLIENT TRACKING ON BCAST PREFIX user: NOLOOP
OK
> CLIENT TRACKINGINFO
1) "flags"
2) 1) "on"
   2) "bcast"
   3) "noloop"
3) "redirect"
4) (integer) 0
5) "prefixes"
6) 1) "user:"
```
