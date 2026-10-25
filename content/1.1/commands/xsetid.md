---
title: "XSETID"
description: "Sets the last ID of the stream at key, so that new entries get greater IDs."
version: "1.1"
command: "XSETID"
syntax: "XSETID key last-id [ENTRIESADDED n] [MAXDELETEDID id]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XSETID key last-id [ENTRIESADDED n] [MAXDELETEDID id]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Sets the last ID of the stream at `key`, so that new entries get greater IDs. `ENTRIESADDED n` sets how many entries the stream counts as ever added, and `MAXDELETEDID id` the greatest ID it counts as deleted; consumer groups use both to work out their lag.

## Reply

- `OK`.

## Examples

```
> XADD s 1-0 t a
"1-0"
> XSETID s 10-0
OK
> XADD s 5-0 a 1
(error) ERR The ID specified in XADD is equal or smaller than the target stream top item
```
