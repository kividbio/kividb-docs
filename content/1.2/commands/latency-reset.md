---
title: "LATENCY RESET"
description: "Clears the samples of every event, or of the events named."
version: "1.2"
command: "LATENCY RESET"
syntax: "LATENCY RESET [event ...]"
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
LATENCY RESET [event ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Clears what the latency monitor has recorded: the samples of every event, or, with names, of those events only. A cleared event leaves [`LATENCY LATEST`](latency-latest.md), [`LATENCY HISTORY`](latency-history.md) and [`LATENCY GRAPH`](latency-graph.md), and its maximum, the fourth field of `LATENCY LATEST`, starts again from the next sample. Use it after fixing a cause of latency, so that what is recorded next is new.

The monitor keeps recording as before: [`latency-monitor-threshold`](../reference/configuration.md#latency-monitor-threshold) is not changed. The per-command figures of [`LATENCY HISTOGRAM`](latency-histogram.md) are kept apart, and are not cleared. A name that is no event's is passed over.

## Reply

The number of events that had samples and were cleared: all of them with no arguments, or those among the names given. `0` if there was nothing to clear.

## Examples

```
> CONFIG SET latency-monitor-threshold 100
OK
> DEBUG SLEEP 0.15
OK
> LATENCY RESET nosuch
(integer) 0
> LATENCY RESET command nosuch
(integer) 1
> LATENCY HISTORY command
(empty array)
> LATENCY RESET
(integer) 0
```
