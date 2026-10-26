---
title: "XINFO CONSUMERS"
description: "Returns, for each consumer of the group: its name, how many entries it has pending, the milliseconds since it last read (idle), and the milliseconds since its last read that returned entries (inactiv…"
version: "1.2"
command: "XINFO CONSUMERS"
syntax: "XINFO CONSUMERS key group"
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
XINFO CONSUMERS key group
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns, for each consumer of the group: its name, how many entries it has pending, the milliseconds since it last read (`idle`), and the milliseconds since its last read that returned entries (`inactive`).

## Examples

```
> XINFO CONSUMERS jobs workers
1) 1) "name"
   2) "alice"
   3) "pending"
   4) (integer) 0
   5) "idle"
   6) (integer) 1
   7) "inactive"
   8) (integer) 1
```
