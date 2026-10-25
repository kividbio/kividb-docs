---
title: "HOTKEYS GET"
description: "Returns the current or latest session: whether it is still running, its settings, its totals, and the top keys by CPU time (by-cpu-time-us) and by network bytes (by-net-bytes)."
version: "1.1"
command: "HOTKEYS GET"
syntax: "HOTKEYS GET"
group: "observability"
since: "1.1.0"
history: []
container: "HOTKEYS"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS GET
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the current or latest session: whether it is still running, its settings, its totals, and the top keys by CPU time (`by-cpu-time-us`) and by network bytes (`by-net-bytes`).

## Reply

- The session, as an array of names and values.
- `nil` if there is none.

## Examples

```
> HOTKEYS GET
1)  1) "tracking-active"
    2) (integer) 1
    ...
   23) "by-cpu-time-us"
   24) 1) "k1"
       2) (integer) 434
       3) "k2"
       4) (integer) 31
   25) "by-net-bytes"
   26) 1) "k1"
       2) (integer) 147
       3) "k2"
       4) (integer) 81
```
