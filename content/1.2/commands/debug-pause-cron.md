---
title: "DEBUG PAUSE-CRON"
description: "DEBUG PAUSE-CRON 1 pauses the background expiry, of keys and hash fields, and DEBUG PAUSE-CRON 0 resumes it, as Redis's pauses its cron, where that expiry runs."
version: "1.2"
command: "DEBUG PAUSE-CRON"
syntax: "DEBUG PAUSE-CRON 0|1"
group: "server"
since: "1.2.1"
history: []
container: "DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG PAUSE-CRON 0|1
```

**Available since:** 1.2.1
<!-- generated: end -->
`DEBUG PAUSE-CRON 1` pauses the background expiry, of keys and hash fields, and `DEBUG PAUSE-CRON 0` resumes it, as Redis's pauses its cron, where that expiry runs. Meanwhile a key or field past its time still goes when a command reads it. Test suites use it to keep keys past their time in place. Since 1.2.1; before, it replied `OK` and did nothing. See [`DEBUG`](debug.md).

## Reply

`OK`.

## Examples

```
> DEBUG PAUSE-CRON 1
OK
> SET k v PX 100
OK
```

A second later, `expired_keys_active` in `INFO stats` has not moved. After `DEBUG PAUSE-CRON 0`, `k` goes within a moment.
