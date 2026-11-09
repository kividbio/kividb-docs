---
title: "CONFIG RESETSTAT"
description: "Resets the statistics INFO reports: commands' counts and times, error counts, and connection and network totals."
version: "1.2"
command: "CONFIG RESETSTAT"
syntax: "CONFIG RESETSTAT"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG RESETSTAT
```

**Available since:** 1.1.0
<!-- generated: end -->
Resets the statistics [`INFO`](info.md) reports, so that they count from now: the number of commands processed and connections received, the network totals, keyspace hits and misses, error counts, and each command's calls and time (`INFO commandstats`, `INFO errorstats`).

Use it before a load test or after a change, to read figures that cover only what follows. What describes the server's state is not reset: the keys, memory in use and its peak (`used_memory_peak`), the uptime and the connected clients.

## Reply

`OK`.

## Examples

```
> INFO stats
...
total_commands_processed:54
keyspace_hits:1
...
> CONFIG RESETSTAT
OK
> INFO stats
...
total_commands_processed:1
keyspace_hits:0
...
```
