---
title: "DEBUG LOG"
description: "Writes message to the server's log, at the WARN level, as DEBUG LOG: <message>."
version: "1.2"
command: "DEBUG LOG"
syntax: "DEBUG LOG message"
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
DEBUG LOG message
```

**Available since:** 1.2.1
<!-- generated: end -->
Writes `message` to the server's log, at the `WARN` level, as `DEBUG LOG: <message>`. Test suites use it to mark where a test starts in the log. Since 1.2.1; before, it replied `OK` and wrote nothing. See [`DEBUG`](debug.md).

## Reply

`OK`.

## Examples

```
> DEBUG LOG test-42-starts
OK
```

In the log:

```
2026-11-12T10:36:24.063Z 11532 [WARN] DEBUG LOG: test-42-starts
```
