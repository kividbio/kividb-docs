---
title: "LATENCY GRAPH"
description: "Draws an event's samples as a small text chart, with the highest and lowest."
version: "1.2"
command: "LATENCY GRAPH"
syntax: "LATENCY GRAPH event"
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
LATENCY GRAPH event
```

**Available since:** 1.1.0
<!-- generated: end -->
Draws an event's samples as a small text chart, with the highest and lowest.

## Reply

- The chart, as a bulk string.
- `ERR No samples for event '<event>'`.

## Examples

```
> LATENCY GRAPH command
command - high 120 ms, low 2 ms (all time high 120 ms)
--------------------------------------------------------------------------------
   _#
   ||
   ||
___||_
```
