---
title: "CLIENT TRACKING"
description: "Enable or disable client-side cache invalidation."
version: "1.2"
command: "CLIENT TRACKING"
syntax: "CLIENT TRACKING ON|OFF [REDIRECT client-id] [BCAST] [PREFIX prefix [...]] [OPTIN] [OPTOUT] [NOLOOP]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLIENT TRACKING ON|OFF [REDIRECT client-id] [BCAST] [PREFIX prefix [...]] [OPTIN] [OPTOUT] [NOLOOP]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Enable or disable client-side cache invalidation. Invalidations reach a RESP3 connection as push messages; a RESP2 connection has to `REDIRECT` them to a connection subscribed to `__redis__:invalidate`, and without `REDIRECT` is sent nothing, as in Redis. Every key a command reads is tracked, and keys written by scripts, expired, evicted or flushed are invalidated. Default mode: all reads auto-register; writers receive their own invalidations. OPTIN: only reads preceded by `CLIENT CACHING yes` are registered. OPTOUT: all reads register unless preceded by `CLIENT CACHING no`. NOLOOP: suppress invalidations sent back to the client that caused the write. REDIRECT forwards invalidations to another client ID. Zero cost when no tracking clients connected — one atomic load per command on the hot path
