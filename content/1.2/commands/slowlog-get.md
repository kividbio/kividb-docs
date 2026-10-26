---
title: "SLOWLOG GET"
description: "Returns the newest entries of the slow log: 10, count, or all of them with -1."
version: "1.2"
command: "SLOWLOG GET"
syntax: "SLOWLOG GET [count]"
group: "observability"
since: "1.1.0"
history: []
container: "SLOWLOG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SLOWLOG GET [count]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the newest entries of the slow log: 10, `count`, or all of them with `-1`.

Each entry has its ID, the Unix time it was logged, how many microseconds the command took, the command and its arguments, the client's address, the client's name, and how many arguments the command had.

## Examples

```
> CONFIG SET slowlog-log-slower-than 0
OK
> GET a
(nil)
> SLOWLOG GET 1
1) 1) (integer) 1
   2) (integer) 1792968201
   3) (integer) 717
   4) 1) "GET"
      2) "a"
   5) "127.0.0.1:57956"
   6) ""
   7) (integer) 2
```
