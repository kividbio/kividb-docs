---
title: "SLOWLOG HELP"
description: "Lists the SLOWLOG subcommands and what each does."
version: "1.2"
command: "SLOWLOG HELP"
syntax: "SLOWLOG HELP"
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
SLOWLOG HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the `SLOWLOG` subcommands, with their arguments and a line on what each does: [`GET`](slowlog-get.md), with the fields of an entry, [`LEN`](slowlog-len.md), [`RESET`](slowlog-reset.md) and `HELP` itself. It changes nothing. Unlike the other `HELP` subcommands, it returns its lines as bulk strings, so `redis-cli` prints them in quotes. The slow log records nothing until [`slowlog-log-slower-than`](../reference/configuration.md#slowlog-log-slower-than) is set; see [Monitoring](../guides/monitoring.md#the-slow-log).

## Reply

An array of lines of text.

## Examples

```
> SLOWLOG HELP
 1) "SLOWLOG <subcommand> [<arg> [value] [opt] ...]. Subcommands are:"
 2) "GET [<count>]"
 3) "    Return top <count> entries from the slowlog (default: 10, -1 mean all)."
 4) "    Entries are made of:"
 5) "    id, timestamp, time in microseconds, arguments array, client IP and port,"
 6) "    client name, total argument count"
 7) "LEN"
 8) "    Return the length of the slowlog."
...
11) "HELP"
12) "    Print this help."
```
