---
title: "DEBUG POPULATE"
description: "Makes count string keys, prefix:0, prefix:1 and on (key:0 and on without a prefix), holding value:0, value:1 and on, cut or padded with zero bytes to size bytes when size is given."
version: "1.2"
command: "DEBUG POPULATE"
syntax: "DEBUG POPULATE count [prefix] [size]"
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
DEBUG POPULATE count [prefix] [size]
```

**Available since:** 1.2.1
<!-- generated: end -->
Makes `count` string keys, `prefix:0`, `prefix:1` and on (`key:0` and on without a prefix), holding `value:0`, `value:1` and on, cut or padded with zero bytes to `size` bytes when `size` is given. A key that is there already is left as it is. Use it to fill a test server quickly.

`COMMAND` lists the `DEBUG` subcommands since 1.2.1, so each has a page; `DEBUG POPULATE` itself makes keys since 1.2. See [`DEBUG`](debug.md).

## Reply

`OK`.

## Examples

```
> DEBUG POPULATE 2
OK
> GET key:0
"value:0"
> DEBUG POPULATE 1 p 12
OK
> STRLEN p:0
(integer) 12
```
