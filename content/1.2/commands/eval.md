---
title: "EVAL"
description: "Runs a Lua script on the server, as one step: no other client's command starts while it runs."
version: "1.2"
command: "EVAL"
syntax: "EVAL script numkeys key [key ...] arg [arg ...]"
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
EVAL script numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
Runs a Lua script on the server, as one step: no other client's command starts while it runs. `numkeys` is how many of the arguments that follow are key names, which the script reads as `KEYS[1]`, `KEYS[2]`, ...; the rest are `ARGV[1]`, `ARGV[2]`, ....

Only the `lua` and `full` builds run scripts. In the default build, every scripting command replies `ERR Lua scripting is not supported by KiviDB`; see [Choose a build](../../1.1/get-started/builds.md).

Inside a script, `redis.call(command, ...)` runs a command and raises its error, if it fails; `redis.pcall` returns the error instead. `redis.error_reply(text)` and `redis.status_reply(text)` make replies.

## Known issue

Refused on a replica with `READONLY`, even for a script that only reads; use [`EVAL_RO`](eval_ro.md) there. Filed as [kividb#145](https://github.com/kividbio/kividb/issues/145).

In a cluster, a `redis.call` on a key in a slot another node owns is not refused: the key is written on this node, where clients will not find it. Filed as [kividb#153](https://github.com/kividbio/kividb/issues/153). Every distinct script is kept in the script cache, with no limit. Filed as [kividb#155](https://github.com/kividbio/kividb/issues/155).

## Reply

What the script returns, converted to RESP:

| Lua | RESP |
|---|---|
| number | integer; a fraction is cut off: `3.7` becomes `3` |
| string | bulk string |
| table with values `1..n` | array |
| `true` | integer `1` |
| `false`, `nil` | `nil` |
| `redis.error_reply(...)`, `{err = ...}` | error |
| `redis.status_reply(...)`, `{ok = ...}` | simple string |

A script that does not compile, or raises an error, replies with the error, naming the script by its SHA1 digest.

## Examples

```
> EVAL "return {KEYS[1], ARGV[1]}" 1 k v
1) "k"
2) "v"
> EVAL "redis.call('SET', KEYS[1], ARGV[1]) return redis.call('GET', KEYS[1])" 1 greeting hi
"hi"
> EVAL "return 3.7" 0
(integer) 3
> EVAL "return redis.error_reply('MY oops')" 0
(error) MY oops
```
