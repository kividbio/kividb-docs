---
title: "XGROUP DESTROY"
description: "Deletes the group, its consumers and its pending entries."
version: "1.2"
command: "XGROUP DESTROY"
syntax: "XGROUP DESTROY key group"
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
XGROUP DESTROY key group
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes the group, its consumers and its pending entries.

## Reply

- `1` if the group existed, `0` if not.

## Examples

```
> XGROUP DESTROY jobs workers
(integer) 1
```
