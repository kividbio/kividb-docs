---
title: "CLUSTER ADDSLOTS"
description: "Makes this node the owner of each slot."
version: "1.2"
command: "CLUSTER ADDSLOTS"
syntax: "CLUSTER ADDSLOTS slot [slot ...]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER ADDSLOTS slot [slot ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Makes this node the owner of each `slot`. Either every slot is assigned or, if one is already owned by any node, or given twice, none is.

A slot it claims is no longer `IMPORTING`, as in Redis. In 1.2.0, the slots before a busy one stayed claimed, without being saved to `nodes.conf` or counted in `CLUSTER INFO`.

## Reply

- `OK`.
- `ERR Slot slot is already busy`.
- `ERR Slot slot specified multiple times`.

## Examples

```
> CLUSTER ADDSLOTS 0 1 2
OK
> CLUSTER ADDSLOTS 1
(error) ERR Slot 1 is already busy
> CLUSTER ADDSLOTS 4 4
(error) ERR Slot 4 specified multiple times
```
