---
title: "HIMPORT DISCARD"
description: "Forgets the fieldset named fieldset on this connection."
version: "1.2"
command: "HIMPORT DISCARD"
syntax: "HIMPORT DISCARD fieldset"
group: "hash"
since: "1.1.0"
history: []
container: "HIMPORT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HIMPORT DISCARD fieldset
```

**Available since:** 1.1.0
<!-- generated: end -->
Forgets the fieldset named `fieldset` on this connection. `HIMPORT DISCARDALL` forgets all of them.

## Reply

- The number of fieldsets forgotten.

## Examples

```
> HIMPORT PREPARE a x
OK
> HIMPORT PREPARE b y
OK
> HIMPORT DISCARD a
(integer) 1
> HIMPORT DISCARDALL
(integer) 1
```
