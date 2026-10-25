---
title: "LATENCY DOCTOR"
description: "Reports, in words, the events whose latest samples were slow: as warnings from 100 ms, as critical from 500 ms."
version: "1.1"
command: "LATENCY DOCTOR"
syntax: "LATENCY DOCTOR"
group: "observability"
since: "1.1.0"
history: []
container: "LATENCY"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LATENCY DOCTOR
```

**Available since:** 1.1.0
<!-- generated: end -->
Reports, in words, the events whose latest samples were slow: as warnings from 100 ms, as critical from 500 ms. With nothing to report, it says so as Redis does.

## Examples

```
> LATENCY DOCTOR
Dave, I have observed the system for some time and I have no problem to report.
```
