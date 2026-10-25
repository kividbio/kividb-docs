---
title: "LATENCY HISTOGRAM"
description: "Returns, for each command named, or every command called, its number of calls and how many of them took less than each power of two of microseconds."
version: "1.2"
command: "LATENCY HISTOGRAM"
syntax: "LATENCY HISTOGRAM [command ...]"
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
LATENCY HISTOGRAM [command ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns, for each command named, or every command called, its number of calls and how many of them took less than each power of two of microseconds. Under RESP3 the reply is a map.

## Examples

```
> LATENCY HISTOGRAM GET SET
1) "get"
2) 1) "calls"
   2) (integer) 1
   3) "histogram_usec"
   4) 1) (integer) 1024
      2) (integer) 1
3) "set"
...
```
