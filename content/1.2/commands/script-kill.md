---
title: "SCRIPT KILL"
description: "Stops the script running, if it has not written anything."
version: "1.2"
command: "SCRIPT KILL"
syntax: "SCRIPT KILL"
group: "scripting"
since: "1.1.0"
history: []
container: "SCRIPT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCRIPT KILL
```

**Available since:** 1.1.0
<!-- generated: end -->
Stops the script running, if it has not written anything. While a script has run longer than `lua-time-limit` (5 seconds by default), other clients' commands get `BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.`. `SCRIPT KILL` and `SHUTDOWN NOSAVE` still get through.

## Reply

- `OK`; the script's client gets `ERR Script killed by user`.
- `ERR No scripts in execution.` if none is running.
- `UNKILLABLE Sorry the script already executed write commands against the dataset.` if the script has written. It runs on, and the server stays busy until it ends or `SHUTDOWN NOSAVE`. Before 1.2, this was answered `OK`, and the script ran on all the same.

## Examples

```
client 1> EVAL "local i=0 while true do end" 0
client 2> GET greeting
(error) BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.
client 2> SCRIPT KILL
OK
client 1>
(error) ERR Script killed by user
```
