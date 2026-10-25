---
title: "CLIENT TRACKINGINFO"
description: "Returns this connection's tracking state: its flags (off, on, bcast, optin, optout, noloop), the connection it redirects to, and its prefixes."
version: "1.1"
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
Returns this connection's tracking state: its flags (`off`, `on`, `bcast`, `optin`, `optout`, `noloop`), the connection it redirects to, and its prefixes.

## Examples

```
> CLIENT TRACKINGINFO
1) "flags"
2) 1) "on"
3) "redirect"
4) (integer) 0
5) "prefixes"
6) (empty array)
```
