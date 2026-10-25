---
title: "CLIENT SETINFO"
description: "Records the client library's name, LIB-NAME, or version, LIB-VER, on the connection; CLIENT LIST shows them as lib-name and lib-ver."
version: "1.1"
command: "CLIENT SETINFO"
syntax: "CLIENT SETINFO LIB-NAME name | LIB-VER ver"
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
CLIENT SETINFO LIB-NAME name | LIB-VER ver
```

**Available since:** 1.1.0
<!-- generated: end -->
Records the client library's name, `LIB-NAME`, or version, `LIB-VER`, on the connection; [`CLIENT LIST`](client-list.md) shows them as `lib-name` and `lib-ver`. Client libraries send it when they connect.

## Examples

```
> CLIENT SETINFO LIB-NAME redis-py
OK
> CLIENT SETINFO LIB-VER 5.0
OK
```
