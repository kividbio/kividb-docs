---
title: "LATENCY HISTORY"
description: "Returns an event's samples, oldest first, each the Unix time and the milliseconds; an empty array for an event with none."
version: "1.2"
command: "LATENCY HISTORY"
syntax: "LATENCY HISTORY event"
group: "observability"
since: "1.1.0"
history: []
container: "LATENCY"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LATENCY HISTORY event
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns an event's samples, oldest first, each the Unix time and the milliseconds; an empty array for an event with none.

## Examples

```
> LATENCY HISTORY command
1) 1) (integer) 1792968201
   2) (integer) 100
2) 1) (integer) 1792968201
   2) (integer) 120
```
