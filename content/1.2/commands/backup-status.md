---
title: "BACKUP STATUS"
description: "Returns the backup's state, its error if it failed, and its start and end times."
version: "1.2"
command: "BACKUP STATUS"
syntax: "BACKUP STATUS"
group: "other"
since: "1.1.0"
history: []
container: "BACKUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BACKUP STATUS
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the backup's `state`, its `error` if it failed, and its start and end times. The states are `idle`, `snapshotting` (writing the snapshot), `incrementing` (collecting writes), `sealed` and `failed`.

## Examples

```
> BACKUP STATUS
1) "state"
2) "incrementing"
3) "error"
4) ""
5) "start_time"
6) "1792968311"
7) "end_time"
8) "0"
```
