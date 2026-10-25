---
title: "XACK"
description: "Acknowledges entries the group delivered: they are no longer pending."
version: "1.2"
command: "XACK"
syntax: "XACK key group id [id ...]"
group: "stream"
since: "1.1.0"
arity: -4
flags: ["fast", "write"]
acl_categories: ["fast", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XACK key group id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@fast`, `@stream`, `@write`
<!-- generated: end -->
Acknowledges entries the group delivered: they are no longer pending.

## Reply

- The number of entries acknowledged; IDs that were not pending are not counted.

## Examples

```
> XACK jobs workers 1-0 9-0
(integer) 1
```
