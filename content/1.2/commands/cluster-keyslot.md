---
title: "CLUSTER KEYSLOT"
description: "Returns the slot of key: the CRC16 of the key, modulo 16384."
version: "1.2"
command: "CLUSTER KEYSLOT"
syntax: "CLUSTER KEYSLOT key"
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
CLUSTER KEYSLOT key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the slot of `key`: the CRC16 of the key, modulo 16384. If the key holds a `{...}` with something between the braces, only that part is hashed, so `{user:1}:cart` and `{user:1}:orders` are in the same slot, and one command can use both.

## Examples

```
> CLUSTER KEYSLOT user:1
(integer) 10778
> CLUSTER KEYSLOT {user:1}:cart
(integer) 10778
```
