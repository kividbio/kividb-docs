---
title: "CLIENT INFO"
description: "Returns this connection's line of CLIENT LIST."
version: "1.2"
command: "CLIENT INFO"
syntax: "CLIENT INFO"
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
CLIENT INFO
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns this connection's line of [`CLIENT LIST`](client-list.md).

## Examples

```
> CLIENT INFO
"id=1 addr=127.0.0.1:51999 laddr=127.0.0.1:6380 fd=0 name=worker-1 age=0 idle=0 flags=N db=0 ... user=default redir=-1 resp=2 lib-name=redis-py lib-ver=5.0 ...\n"
```
