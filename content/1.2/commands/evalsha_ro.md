---
title: "EVALSHA_RO"
description: "Runs a script the server already has, named by its SHA1 digest, as EVALSHA does, on the condition that the script only reads: a command in it that writes fails, and the script stops with that error."
version: "1.2"
command: "EVALSHA_RO"
syntax: "EVALSHA_RO sha1 numkeys key [key ...] arg [arg ...]"
group: "scripting"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["scripting", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
EVALSHA_RO sha1 numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
Runs a script the server already has, named by its SHA1 digest, as [`EVALSHA`](evalsha.md) does, on the condition that the script only reads: a command in it that writes fails, and the script stops with that error. It is to `EVALSHA` what [`EVAL_RO`](eval_ro.md) is to [`EVAL`](eval.md). A script that cannot write can be sent to a replica, so read-only scripts can be spread over a database's replicas.

- `sha1`: the digest [`SCRIPT LOAD`](script-load.md) returned, or that of a script sent before with `EVAL`.
- `numkeys`, the keys, then the other arguments, as for `EVALSHA`.

A script loaded with `SCRIPT LOAD` on the master is copied to its replicas, so `EVALSHA_RO` finds it there too.

Lua is in the `lua` and `full` builds only. The default build answers every scripting command, this one included, with an error that says so; see [Scripting](../guides/scripting.md#builds-with-lua).

## Reply

What the script returns, as for `EVAL`.

## Errors

- `NOSCRIPT No matching script. Please use EVAL.` if the server does not have the script: after a restart or [`SCRIPT FLUSH`](script-flush.md), for example. `EVAL_RO` sends the script itself.
- `ERR Write commands are not allowed from read-only scripts. ...` if the script runs a command that writes. Nothing is written.
- In the default build: `ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.1-lua, or a kividb-lua release file)`.

## Examples

```
> SET greeting hi
OK
> SCRIPT LOAD "return redis.call('GET', KEYS[1])"
"d3c21d0c2b9ca22f82737626a27bcaf5d288f99f"
> EVALSHA_RO d3c21d0c2b9ca22f82737626a27bcaf5d288f99f 1 greeting
"hi"
> SCRIPT LOAD "return redis.call('SET', KEYS[1], ARGV[1])"
"d8f2fad9f8e86a53d2a6ebd960b33c4972cacc37"
> EVALSHA_RO d8f2fad9f8e86a53d2a6ebd960b33c4972cacc37 1 greeting bye
(error) ERR Write commands are not allowed from read-only scripts. script: d8f2fad9f8e86a53d2a6ebd960b33c4972cacc37, on @user_script:1.
> EVALSHA_RO ffffffffffffffffffffffffffffffffffffffff 0
(error) NOSCRIPT No matching script. Please use EVAL.
```
