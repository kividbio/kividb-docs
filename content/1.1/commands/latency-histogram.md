---
title: "LATENCY HISTOGRAM"
description: "Per command, its number of calls and how many took less than each power of two of microseconds (calls, histogram_usec) — a map under RESP3."
version: "1.1"
command: "LATENCY HISTOGRAM"
syntax: "LATENCY HISTOGRAM [command ...]"
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
LATENCY HISTOGRAM [command ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Per command, its number of calls and how many took less than each power of two of microseconds (`calls`, `histogram_usec`) — a map under RESP3. With no arguments, every command that has been called
