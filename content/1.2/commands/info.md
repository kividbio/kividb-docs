---
title: "INFO"
description: "Returns information and statistics about the server, as field:value lines in sections."
version: "1.2"
command: "INFO"
syntax: "INFO [section [section ...]]"
group: "server"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
INFO [section [section ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Returns information and statistics about the server, as `field:value` lines in sections. With no section, the default ones, which leave out `commandstats`, `latencystats` and `keysizes`; with `all` or `everything`, all of them.

Sections include `server`, `clients`, `memory`, `persistence`, `stats`, `replication`, `cpu`, `modules`, `commandstats`, `latencystats`, `errorstats`, `cluster`, `keyspace` and `keysizes`. `commandstats` gives each command's calls, time and failures, with Redis 8.8's slow-log fields. `latencystats` gives percentiles of each command's run time. `memory` gives `used_memory`, which `maxmemory` is compared with, `used_memory_rss`, and `mem_fragmentation_ratio`, the one over the other. `keysizes` looks at every key: asked for by name, it counts them each time; in `INFO all` or `everything`, it gives a count up to 10 seconds old.

Before 1.2, `total_commands_processed`, `keyspace_hits` and `keyspace_misses` stayed `0` on a quiet server, `total_reads_processed` and `total_writes_processed` were always `0`, and `mem_fragmentation_ratio` was the process's virtual size over its resident size. See [Monitoring](../guides/monitoring.md) for the fields worth watching.

## Examples

```
> INFO commandstats
# Commandstats
cmdstat_get:calls=3,usec=59,usec_per_call=19.67,rejected_calls=0,failed_calls=0
...
```
