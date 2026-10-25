---
title: "XGROUP CREATECONSUMER"
description: "Creates the consumer consumer in the group."
version: "1.1"
command: "XGROUP CREATECONSUMER"
syntax: "XGROUP CREATECONSUMER key group consumer"
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
XGROUP CREATECONSUMER key group consumer
```

**Available since:** 1.1.0
<!-- generated: end -->
Creates the consumer `consumer` in the group. Consumers are also created the first time they read.

## Reply

- `1` if created, `0` if it existed.

## Examples

```
> XGROUP CREATECONSUMER jobs workers dave
(integer) 1
```
