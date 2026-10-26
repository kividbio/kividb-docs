---
title: "LATENCY RESET"
description: "Clears the samples of every event, or of the events named."
version: "1.1"
command: "LATENCY RESET"
syntax: "LATENCY RESET [event ...]"
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
LATENCY RESET [event ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Clears the samples of every event, or of the events named.

## Reply

- The number of events that had samples.

## Examples

```
> LATENCY RESET
(integer) 2
```
