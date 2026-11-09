---
title: "SCRIPT LOAD"
description: "Puts a script in the server's cache, without running it, and returns its SHA1 digest."
version: "1.2"
command: "SCRIPT LOAD"
syntax: "SCRIPT LOAD script"
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
SCRIPT LOAD script
```

**Available since:** 1.1.0
<!-- generated: end -->
Puts a script in the server's cache, without running it, and returns its SHA1 digest. [`EVALSHA`](evalsha.md) and [`EVALSHA_RO`](evalsha_ro.md) then run it by that digest, so a client sends a long script once rather than with every call.

- `script`: the Lua source, which must be UTF-8. The digest is the SHA1 of exactly these bytes, as Redis computes it, so the same script has the same digest on every server. Loading it again changes nothing and returns the same digest.

KiviDB does not compile the script when it is loaded: a script with a syntax error is cached and gets its digest, and the error comes when the script is run. Redis compiles it, and refuses it with an error at once.

A script loaded this way stays until [`SCRIPT FLUSH`](script-flush.md) or a restart; it is not one of the 500 scripts sent with `EVAL` that the server keeps and lets go of. `SCRIPT LOAD` on the master loads the script on its replicas too. On a replica, it is refused with `READONLY`. Redis 7 takes it on a replica, and does not pass it on to replicas. See [Scripting](../guides/scripting.md#scripts).

`SCRIPT LOAD` is in the `lua` and `full` builds only. The default build answers it, like every `SCRIPT` subcommand, with `ERR this build of KiviDB has no Lua: ...`.

## Reply

The script's SHA1 digest, 40 lower-case hex characters.

## Examples

```
> SCRIPT LOAD "return ARGV[1]"
"098e0f0d1448c0a81dafe820f66d460eb09263da"
> EVALSHA 098e0f0d1448c0a81dafe820f66d460eb09263da 0 hello
"hello"
> SCRIPT LOAD "return ("
"728acb63e2aaef0ee859ece5db586bff5d800d1e"
> EVALSHA 728acb63e2aaef0ee859ece5db586bff5d800d1e 0
(error) ERR user_script:1: unexpected symbol near <eof> script: 728acb63e2aaef0ee859ece5db586bff5d800d1e, on @user_script:1.
```
