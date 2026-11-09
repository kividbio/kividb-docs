---
title: "SLOWLOG LEN"
description: "Returns how many entries the slow log holds now."
version: "1.2"
command: "SLOWLOG LEN"
syntax: "SLOWLOG LEN"
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
SLOWLOG LEN
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns how many entries the slow log holds now. Use it to see whether anything has been logged before reading the entries with [`SLOWLOG GET`](slowlog-get.md).

It is at most [`slowlog-max-len`](../reference/configuration.md#slowlog-max-len) (128 by default): when the log is full, each new entry pushes out the oldest. It is `0` while the log is off, which it is by default ([`slowlog-log-slower-than`](../reference/configuration.md#slowlog-log-slower-than) `-1`), and after [`SLOWLOG RESET`](slowlog-reset.md). It is not the number of slow commands ever logged: `slowlog_commands_count` in `INFO stats` counts those, and `SLOWLOG RESET` does not clear it.

A command is logged after it has run, so with a threshold of `0`, `SLOWLOG LEN` is itself in the log by the next call.

## Reply

The number of entries, as an integer.

## Examples

```
> CONFIG SET slowlog-log-slower-than 0
OK
> SET a 1
OK
> GET a
"1"
> SLOWLOG LEN
(integer) 2
> CONFIG SET slowlog-max-len 3
OK
> INCR n
(integer) 1
> INCR n
(integer) 2
> SLOWLOG LEN
(integer) 3
```
