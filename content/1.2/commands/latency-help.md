---
title: "LATENCY HELP"
description: "Lists the LATENCY subcommands and what each does."
version: "1.2"
command: "LATENCY HELP"
syntax: "LATENCY HELP"
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
LATENCY HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `LATENCY` subcommands, with their arguments and a line on what each does: [`DOCTOR`](latency-doctor.md), [`GRAPH`](latency-graph.md), [`HISTORY`](latency-history.md), [`LATEST`](latency-latest.md), [`RESET`](latency-reset.md), [`HISTOGRAM`](latency-histogram.md) and `HELP` itself. It changes nothing. The latency monitor records events only once [`latency-monitor-threshold`](../reference/configuration.md#latency-monitor-threshold) is set; see [Monitoring](../guides/monitoring.md#the-latency-monitor).

## Reply

An array of lines of text.

## Examples

```
> LATENCY HELP
 1) LATENCY <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) DOCTOR
 3)     Return a human readable latency analysis report.
 4) GRAPH <event>
 5)     Return an ASCII latency graph for the <event> class.
 6) HISTORY <event>
 7)     Return time-latency samples for the <event> class.
...
16) HELP
17)     Print this help.
```
