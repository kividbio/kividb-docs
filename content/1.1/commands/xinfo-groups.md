---
title: "XINFO GROUPS"
description: "Returns, for each consumer group of the stream: its name, its consumers' count, its pending entries' count, the last ID it delivered, how many entries it has read, and its lag, how many entries it ha…"
version: "1.1"
command: "XINFO GROUPS"
syntax: "XINFO GROUPS key"
group: "stream"
since: "1.1.0"
history: []
container: "XINFO"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XINFO GROUPS key
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns, for each consumer group of the stream: its name, its consumers' count, its pending entries' count, the last ID it delivered, how many entries it has read, and its lag, how many entries it has yet to deliver.

## Examples

```
> XINFO GROUPS jobs
1) 1) "name"
   2) "workers"
   3) "consumers"
   4) (integer) 3
   5) "pending"
   6) (integer) 2
   7) "last-delivered-id"
   8) "3-0"
   9) "entries-read"
  10) (integer) 3
  11) "lag"
  12) (integer) 0
```
