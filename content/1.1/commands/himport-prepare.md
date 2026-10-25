---
title: "HIMPORT PREPARE"
description: "Defines a fieldset named fieldset on this connection: the field names that HIMPORT SET gives values for, in order."
version: "1.1"
command: "HIMPORT PREPARE"
syntax: "HIMPORT PREPARE fieldset field [field ...]"
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
HIMPORT PREPARE fieldset field [field ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Defines a fieldset named `fieldset` on this connection: the field names that [`HIMPORT SET`](himport-set.md) gives values for, in order. Defining it again replaces it.

## Reply

- `OK`.

## Examples

```
> HIMPORT PREPARE person name lang
OK
```
