---
title: "LATENCY"
description: "The latency monitor: it records, for each kind of event, the times it took longer than latency-monitor-threshold milliseconds, which is 0, off, by default."
version: "1.1"
command: "LATENCY"
syntax: "LATENCY"
group: "observability"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["LATENCY DOCTOR", "LATENCY GRAPH", "LATENCY HELP", "LATENCY HISTOGRAM", "LATENCY HISTORY", "LATENCY LATEST", "LATENCY RESET"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LATENCY
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [LATENCY DOCTOR](latency-doctor.md), [LATENCY GRAPH](latency-graph.md), [LATENCY HELP](latency-help.md), [LATENCY HISTOGRAM](latency-histogram.md), [LATENCY HISTORY](latency-history.md), [LATENCY LATEST](latency-latest.md), [LATENCY RESET](latency-reset.md)
<!-- generated: end -->
The latency monitor: it records, for each kind of event, the times it took longer than `latency-monitor-threshold` milliseconds, which is `0`, off, by default. Events include `command` (a slow command), `fast-command` (a slow `O(1)` or `O(log N)` one), and `expire-cycle` (expiring keys in the background). See its subcommands.
