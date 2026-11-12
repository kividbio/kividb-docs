---
title: "CONFIG RESETSTAT"
description: "Resets the statistics INFO reports, so that they count from now: the number of commands processed and connections received, the network totals, keyspace hits and misses, error counts, and each comman…"
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

Use it before a load test or after a change, to read figures that cover only what follows. What describes the server's state is not reset: the keys, memory in use and its peak (`used_memory_peak`), the uptime, the connected clients, `rdb_changes_since_last_save` and `active_defrag_disabled_by_panics`. Active defrag's counters, `active_defrag_hits`, `active_defrag_misses` and `active_defrag_panics`, are reset, as in Redis. Both are since 1.2.1: 1.2.0 reset `rdb_changes_since_last_save` and kept the active defrag counters.

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
