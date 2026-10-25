---
title: "INFO"
description: "Return server info; sections include server, keyspace, replication, errorstats (per-error reply counters), all, etc."
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
status: "draft"
---

<!-- generated: start -->
## Syntax

```
INFO [section [section ...]]
```

**Available since:** 1.1.0 · **ACL categories:** `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
## Description

Return server info; sections include `server`, `keyspace`, `replication`, `errorstats` (per-error reply counters), `all`, etc. `INFO commandstats` has, for each command that has been called, `calls`, `usec`, `usec_per_call`, `rejected_calls` and `failed_calls`, and the Redis 8.8 slowlog fields `slowlog_count`, `slowlog_time_ms_sum` and `slowlog_time_ms_max`. `INFO memory` reports `used_memory` (allocated bytes — what `maxmemory` is compared with), `used_memory_rss`, `maxmemory_policy`, the slabs of string values (`value_slab_bytes`, and `value_slab_live_bytes` in them) and active defrag's `active_defrag_running`, `active_defrag_hits` (values moved) and `active_defrag_misses` (left, being held); `INFO stats` reports `evicted_keys`
