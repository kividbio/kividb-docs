---
title: "LATENCY DOCTOR"
description: "Return a human-readable diagnostic report."
version: "1.1"
command: "LATENCY DOCTOR"
syntax: "LATENCY DOCTOR"
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
LATENCY DOCTOR
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Return a human-readable diagnostic report. Flags events whose latest sample exceeds warning (≥100ms) or critical (≥500ms) thresholds. Returns Redis's exact clean-bill-of-health message when no issues are detected
