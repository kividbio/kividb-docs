---
title: "SLOWLOG RESET"
description: "Empties the slow log."
version: "1.2"
command: "SLOWLOG RESET"
syntax: "SLOWLOG RESET"
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
SLOWLOG RESET
```

**Available since:** 1.1.0
<!-- generated: end -->
Empties the slow log: [`SLOWLOG GET`](slowlog-get.md) and [`SLOWLOG LEN`](slowlog-len.md) start again from nothing. Use it before a test, or after reading the entries, so that what is logged next is new.

It does not turn the log off or change its settings: commands slower than [`slowlog-log-slower-than`](../reference/configuration.md#slowlog-log-slower-than) are still logged, and `SLOWLOG RESET` is logged itself when it qualifies, so with a threshold of `0` the log holds one entry straight after. Entry IDs carry on from where they were rather than starting at `0` again. The totals in `INFO stats`, `slowlog_commands_count` and `slowlog_commands_time_ms_sum`, are not reset; [`CONFIG RESETSTAT`](config-resetstat.md) is the command for statistics.

## Reply

`OK`.

## Examples

```
> CONFIG SET slowlog-log-slower-than 0
OK
> SET a 1
OK
> GET a
"1"
> SLOWLOG RESET
OK
> SLOWLOG GET
1) 1) (integer) 2
   2) (integer) 1794254762
   3) (integer) 18
   4) 1) "SLOWLOG"
      2) "RESET"
   5) "127.0.0.1:39490"
   6) ""
   7) (integer) 2
```
