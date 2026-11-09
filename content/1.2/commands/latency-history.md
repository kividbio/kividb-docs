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
Returns the samples the latency monitor has recorded for one event, oldest first: for each, the Unix time in seconds and how many milliseconds it took. Use it to see when an event was slow and whether it is getting worse; [`LATENCY LATEST`](latency-latest.md) gives only each event's last sample, and [`LATENCY GRAPH`](latency-graph.md) draws the same samples as a chart.

`event` is one of the monitor's event names, such as `command`, `fast-command` or `expire-cycle` (see [`LATENCY`](latency.md)). Names are lower case and matched exactly: `COMMAND` is not `command`. An event with no samples, or a name that is no event's, gives an empty array.

Samples are recorded only while [`latency-monitor-threshold`](../reference/configuration.md#latency-monitor-threshold) is above `0`, its default, for what took at least that many milliseconds. Each event keeps its last 180 samples, the oldest going first. Every sample is kept, even two in the same second, where Redis keeps 160, one a second, the highest. [`LATENCY RESET`](latency-reset.md) clears them.

## Reply

An array of `[time, milliseconds]` pairs; an empty array if there are none.

## Examples

```
> CONFIG SET latency-monitor-threshold 100
OK
> DEBUG SLEEP 0.25
OK
> DEBUG SLEEP 0.15
OK
> LATENCY HISTORY command
1) 1) (integer) 1794254263
   2) (integer) 250
2) 1) (integer) 1794254263
   2) (integer) 150
> LATENCY HISTORY expire-cycle
(empty array)
> LATENCY HISTORY
(error) ERR wrong number of arguments for 'latency|history' command
```
