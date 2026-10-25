---
title: "CLUSTER COUNTKEYSINSLOT"
description: "Returns the number of keys this node holds in slot."
version: "1.1"
command: "CLUSTER COUNTKEYSINSLOT"
syntax: "CLUSTER COUNTKEYSINSLOT slot"
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
CLUSTER COUNTKEYSINSLOT slot
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the number of keys this node holds in `slot`.

## Reply

- The number of keys.
- `ERR Invalid slot slot, must be between 0 and 16383`.

## Examples

```
> CLUSTER COUNTKEYSINSLOT 15495
(integer) 2
```
