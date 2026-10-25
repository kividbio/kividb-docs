---
title: "LATENCY GRAPH"
description: "Return a UTF-8 sparkline string (up to 80 chars, using ▁▂▃▄▅▆▇█) visualising the history of event."
version: "1.1"
command: "LATENCY GRAPH"
syntax: "LATENCY GRAPH event"
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
LATENCY GRAPH event
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return a UTF-8 sparkline string (up to 80 chars, using `▁▂▃▄▅▆▇█`) visualising the history of `event`. Returns an error if the event has no samples
