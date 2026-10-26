---
title: "CLIENT SETNAME"
description: "Names the connection; the name shows in CLIENT LIST."
version: "1.1"
command: "CLIENT SETNAME"
syntax: "CLIENT SETNAME name"
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
CLIENT SETNAME name
```

**Available since:** 1.1.0
<!-- generated: end -->
Names the connection; the name shows in [`CLIENT LIST`](client-list.md). Names cannot contain spaces, newlines or special characters. An empty name removes it.

## Examples

```
> CLIENT SETNAME worker-1
OK
> CLIENT SETNAME "has space"
(error) ERR Client names cannot contain spaces, newlines or special characters.
```
