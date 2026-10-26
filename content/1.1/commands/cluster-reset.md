---
title: "CLUSTER RESET"
description: "Clears this node's topology: it forgets the other nodes and which slots it owns, and becomes a master with no slots."
version: "1.1"
command: "CLUSTER RESET"
syntax: "CLUSTER RESET [HARD | SOFT]"
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
CLUSTER RESET [HARD | SOFT]
```

**Available since:** 1.1.0
<!-- generated: end -->
Clears this node's topology: it forgets the other nodes and which slots it owns, and becomes a master with no slots.

| Option | Effect |
|---|---|
| `SOFT` | The default. Keeps the node ID and the epochs. Refused on a master that holds keys. |
| `HARD` | Also deletes every key, resets the epochs, and gives the node a new ID. |

## Reply

- `OK`.
- `ERR CLUSTER RESET can't be called with master nodes containing keys`.

## Examples

```
> CLUSTER RESET HARD
OK
```
