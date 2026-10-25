---
title: "LATENCY HISTORY"
description: "Return all stored samples for event in chronological order as [[timestamp_secs, latency_ms], ...]."
version: "1.2"
command: "LATENCY HISTORY"
syntax: "LATENCY HISTORY event"
group: "observability"
since: "1.1.0"
history: []
container: "LATENCY"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
LATENCY HISTORY event
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return all stored samples for `event` in chronological order as `[[timestamp_secs, latency_ms], ...]`. Returns an empty array for unknown events
