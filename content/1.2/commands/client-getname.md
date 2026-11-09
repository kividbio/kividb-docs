---
title: "CLIENT GETNAME"
description: "Returns the connection's name, or nil."
version: "1.2"
command: "CLIENT GETNAME"
syntax: "CLIENT GETNAME"
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
CLIENT GETNAME
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the name the connection was given with [`CLIENT SETNAME`](client-setname.md), or `nil` when it has none. A connection starts without a name, and `CLIENT SETNAME ""` takes its name away again.

Names make connections easy to find: they show as `name=` in [`CLIENT LIST`](client-list.md) and [`CLIENT INFO`](client-info.md), and many client libraries set one from a setting such as `client_name`.

## Reply

The name, as a bulk string, or `nil`.

## Examples

```
> CLIENT GETNAME
(nil)
> CLIENT SETNAME worker-1
OK
> CLIENT GETNAME
"worker-1"
> CLIENT SETNAME ""
OK
> CLIENT GETNAME
(nil)
```
