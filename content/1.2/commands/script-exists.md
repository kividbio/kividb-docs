---
title: "SCRIPT EXISTS"
description: "Tells, for each SHA1 digest given, whether the server has that script in its cache, so that EVALSHA can run it."
version: "1.2"
command: "SCRIPT EXISTS"
syntax: "SCRIPT EXISTS sha1 [sha1 ...]"
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
SCRIPT EXISTS sha1 [sha1 ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Tells, for each SHA1 digest given, whether the server has that script in its cache, so that [`EVALSHA`](evalsha.md) can run it. A client can check before a pipeline of `EVALSHA` calls, and send the scripts the server lacks with [`SCRIPT LOAD`](script-load.md) first, rather than handle `NOSCRIPT` errors one by one.

- `sha1 [sha1 ...]`: one or more digests. Case does not matter. A string that is not a digest gets `0`.

The cache holds the scripts loaded with `SCRIPT LOAD`, and, of those sent with [`EVAL`](eval.md), the 500 used most recently. It is emptied by [`SCRIPT FLUSH`](script-flush.md) and by a restart. Functions are not in it: [`FUNCTION LIST`](function-list.md) lists those. See [Scripting](../guides/scripting.md#scripts).

`SCRIPT EXISTS` is in the `lua` and `full` builds only. The default build answers it, like every `SCRIPT` subcommand, with `ERR this build of KiviDB has no Lua: ...`.

## Reply

An array with, for each digest in the order given, `1` if the script is cached and `0` if not.

## Examples

```
> SCRIPT LOAD "return ARGV[1]"
"098e0f0d1448c0a81dafe820f66d460eb09263da"
> SCRIPT EXISTS 098e0f0d1448c0a81dafe820f66d460eb09263da ffffffffffffffffffffffffffffffffffffffff
1) (integer) 1
2) (integer) 0
> SCRIPT EXISTS 098E0F0D1448C0A81DAFE820F66D460EB09263DA
1) (integer) 1
> SCRIPT EXISTS
(error) ERR wrong number of arguments for 'script|exists' command
```
