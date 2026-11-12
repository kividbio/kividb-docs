---
title: "DEBUG SLEEP"
description: "Makes the worker thread that runs it sleep for seconds, which can have a fraction, such as 0.5."
version: "1.2"
command: "DEBUG SLEEP"
syntax: "DEBUG SLEEP seconds"
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
DEBUG SLEEP seconds
```

**Available since:** 1.2.1
<!-- generated: end -->
Makes the worker thread that runs it sleep for `seconds`, which can have a fraction, such as `0.5`. The clients that share that thread wait too; those of other threads do not. Use it to test timeouts and slow-command handling.

`COMMAND` lists the `DEBUG` subcommands since 1.2.1, so each has a page; `DEBUG SLEEP` itself is older. See [`DEBUG`](debug.md).

## Reply

`OK`, once the time has passed.

## Examples

```
> DEBUG SLEEP 0.5          (half a second later)
OK
> DEBUG SLEEP
(error) ERR wrong number of arguments for DEBUG sleep
```
