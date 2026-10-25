---
title: "XINFO STREAM"
description: "Returns the stream's length, its first and last entries and IDs, how many entries it has ever had and the greatest it has deleted, its consumer groups' count, and its idempotent-ID settings and count…"
version: "1.2"
command: "XINFO STREAM"
syntax: "XINFO STREAM key [FULL [COUNT n]]"
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
XINFO STREAM key [FULL [COUNT n]]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the stream's length, its first and last entries and IDs, how many entries it has ever had and the greatest it has deleted, its consumer groups' count, and its idempotent-ID settings and counters. `FULL` adds every group and pending entry; `COUNT n` limits how many of each.

## Examples

```
> XINFO STREAM s
 1) "length"
 2) (integer) 4
 ...
 7) "last-generated-id"
 8) "10-0"
 ...
13) "groups"
14) (integer) 0
15) "idmp-duration"
16) (integer) 100
 ...
```
