---
title: "SWAPDB"
description: "Swaps the contents of two databases in one step, keys and expiries together."
version: "1.1"
command: "SWAPDB"
syntax: "SWAPDB db1 db2"
group: "generic"
since: "1.1.0"
arity: 3
flags: ["write"]
acl_categories: ["dangerous", "server", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SWAPDB db1 db2
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`, `@write`
<!-- generated: end -->
Swaps the contents of two databases in one step, keys and expiries together. Clients connected to either see the other's keys from then on.

## Reply

- `OK`.

## Examples

```
> SWAPDB 0 1
OK
```
