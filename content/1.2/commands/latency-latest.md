---
title: "LATENCY LATEST"
description: "Returns each event's latest sample: the event, the Unix time, and the milliseconds it took."
version: "1.2"
command: "LATENCY LATEST"
syntax: "LATENCY LATEST"
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
LATENCY LATEST
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns each event's latest sample: the event, the Unix time, and the milliseconds it took.

## Examples

```
> CONFIG SET latency-monitor-threshold 50
OK
> DEBUG SLEEP 0.12
OK
> LATENCY LATEST
1) 1) "command"
   2) (integer) 1792968201
   3) (integer) 120
```
