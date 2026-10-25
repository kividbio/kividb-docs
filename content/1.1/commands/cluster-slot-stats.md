---
title: "CLUSTER SLOT-STATS"
description: "Per-slot stats."
version: "1.1"
command: "CLUSTER SLOT-STATS"
syntax: "CLUSTER SLOT-STATS SLOTSRANGE start end` or `CLUSTER SLOT-STATS ORDERBY metric [LIMIT n] [ASC | DESC]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLUSTER SLOT-STATS SLOTSRANGE start end` or `CLUSTER SLOT-STATS ORDERBY metric [LIMIT n] [ASC | DESC]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Per-slot stats. Only `key-count` carries real data; `cpu-usec` / `network-bytes-in` / `network-bytes-out` are reported as 0 (no per-slot instrumentation yet). `ORDERBY` only accepts `key-count`.
