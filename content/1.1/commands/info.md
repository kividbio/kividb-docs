---
title: "INFO"
description: "Returns information and statistics about the server, as field:value lines in sections."
version: "1.1"
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
Returns information and statistics about the server, as `field:value` lines in sections. With no section, the default ones; with `all` or `everything`, all of them.

Sections include `server`, `clients`, `memory`, `persistence`, `stats`, `replication`, `cpu`, `modules`, `commandstats`, `latencystats`, `errorstats`, `cluster` and `keyspace`. `commandstats` gives each command's calls, time and failures, with Redis 8.8's slow-log fields. `memory` gives `used_memory`, which `maxmemory` is compared with, and `used_memory_rss`.

## Known issue

`total_commands_processed`, `total_reads_processed`, `keyspace_hits` and `keyspace_misses` in `INFO stats` stay `0`, while `INFO commandstats` counts commands. Filed as [kividb#136](https://github.com/kividbio/kividb/issues/136), fixed in 1.2.

In `INFO memory`, `mem_fragmentation_ratio` is the process's virtual size over its resident size on Linux, not `used_memory_rss / used_memory`, and several fields are fixed. Filed as [kividb#152](https://github.com/kividbio/kividb/issues/152), fixed in 1.2.

## Examples

```
> INFO commandstats
# Commandstats
cmdstat_get:calls=3,usec=59,usec_per_call=19.67,rejected_calls=0,failed_calls=0
...
```
