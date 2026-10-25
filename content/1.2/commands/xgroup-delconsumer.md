---
title: "XGROUP DELCONSUMER"
description: "Deletes the consumer consumer from the group, with its pending entries: they are no longer pending for anyone."
version: "1.2"
command: "XGROUP DELCONSUMER"
syntax: "XGROUP DELCONSUMER key group consumer"
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
XGROUP DELCONSUMER key group consumer
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes the consumer `consumer` from the group, with its pending entries: they are no longer pending for anyone.

## Reply

- The number of pending entries it had.

## Examples

```
> XGROUP DELCONSUMER jobs workers carol
(integer) 2
```
