---
title: "XGROUP SETID"
description: "Sets the ID the group delivers after: 0 to deliver every entry again, $ to skip to the end."
version: "1.2"
command: "XGROUP SETID"
syntax: "XGROUP SETID key group id|$ [ENTRIESREAD n]"
group: "stream"
since: "1.1.0"
history: []
container: "XGROUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP SETID key group id|$ [ENTRIESREAD n]
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets the ID the group delivers after: `0` to deliver every entry again, `$` to skip to the end. `ENTRIESREAD n` sets how many entries it counts as read.

## Reply

- `OK`.

## Examples

```
> XGROUP SETID jobs workers 0
OK
```
