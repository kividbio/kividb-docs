---
title: "UNWATCH"
description: "Stops watching every key this connection watches."
version: "1.2"
command: "UNWATCH"
syntax: "UNWATCH"
group: "transaction"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["fast", "transaction"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
UNWATCH
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@transaction`
<!-- generated: end -->
Stops watching every key this connection watches.

## Reply

- `OK`.

## Examples

```
> WATCH bal
OK
> UNWATCH
OK
```
