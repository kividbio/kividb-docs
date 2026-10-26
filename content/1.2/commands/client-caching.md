---
title: "CLIENT CACHING"
description: "CLIENT CACHING yes makes the next read of an OPTIN connection be remembered; CLIENT CACHING no makes the next read of an OPTOUT one be skipped."
version: "1.2"
command: "CLIENT CACHING"
syntax: "CLIENT CACHING yes|no"
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
CLIENT CACHING yes|no
```

**Available since:** 1.1.0
<!-- generated: end -->
`CLIENT CACHING yes` makes the next read of an `OPTIN` connection be remembered; `CLIENT CACHING no` makes the next read of an `OPTOUT` one be skipped. See [`CLIENT TRACKING`](client-tracking.md).

## Reply

- `OK`.
- `ERR CLIENT CACHING can be called only when the client is in tracking mode with OPTIN or OPTOUT mode enabled`.
