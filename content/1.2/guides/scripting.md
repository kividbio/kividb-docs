---
title: "Scripting"
description: "Run Lua on the server with EVAL and functions: which builds have it, how scripts run alongside each other, and how they differ from Redis's."
version: "1.2"
weight: 70
---

A script is Lua code the server runs as one step: it reads and writes keys with `redis.call`, and no other client's command runs in the middle of it. KiviDB has Redis's two kinds: scripts sent with [`EVAL`](../commands/eval.md), and libraries of functions loaded with [`FUNCTION LOAD`](../commands/function-load.md) and called with [`FCALL`](../commands/fcall.md).

## Builds with Lua

Lua is in the `lua` and `full` builds only; see [Choose a build](../get-started/builds.md). The default build, which carries the highest throughput, has none, and answers:

```
> EVAL "return 1" 0
(error) ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.0-rc3-lua, or a kividb-lua release file)
```

Job queues that run on scripts, BullMQ and Sidekiq among them, need a build with Lua. Before 1.2, the error said `Lua scripting is not supported by KiviDB`, which read as if no build had it.

The language is Lua 5.4, not Redis's 5.1. Most scripts written for Redis run unchanged; the differences are listed [below](#differences-from-redis).

## Scripts

```
> EVAL "return redis.call('INCRBY', KEYS[1], ARGV[1])" 1 counter 5
(integer) 5
> SCRIPT LOAD "return redis.call('GET', KEYS[1])"
"d3c21d0c2b9ca22f82737626a27bcaf5d288f99f"
> EVALSHA d3c21d0c2b9ca22f82737626a27bcaf5d288f99f 1 counter
"5"
```

Name every key the script uses in `KEYS`, and pass every other value in `ARGV`, rather than writing them into the script: a cluster sends the script to the node that owns its keys, scripts run alongside each other by their keys (below), and the server keeps one compiled copy of each distinct script.

[`EVAL_RO`](../commands/eval_ro.md) and [`EVALSHA_RO`](../commands/evalsha_ro.md) run a script that may only read. A first line `#!lua flags=no-writes` does the same for `EVAL`; `allow-oom` lets a script run while the server is over [`maxmemory`](memory.md).

Scripts are kept by their SHA1. One loaded with [`SCRIPT LOAD`](../commands/script-load.md) stays until [`SCRIPT FLUSH`](../commands/script-flush.md). Of those sent only with `EVAL`, the server keeps the 500 used most recently, as Redis 7.4 does: running one with `EVAL` or `EVALSHA` counts as a use, and `evicted_scripts` in `INFO stats` counts the ones let go. No script is kept across a restart, or on a replica that took its master's place. A client that gets `NOSCRIPT` from `EVALSHA` sends the script again with `EVAL`; client libraries do that on their own. Before 1.2, every script sent with `EVAL` was kept, with no limit.

`redis.log(redis.LOG_WARNING, 'text')` writes its arguments, joined by spaces, to the server's log, at the level given; a level below [`loglevel`](../reference/configuration.md#loglevel) is left out. Before 1.2, `redis.log` did nothing.

## Functions

A library is loaded once, with a name, and kept: it is in the snapshot, it survives a restart, and it is copied to replicas.

```
> FUNCTION LOAD "#!lua name=counters\nredis.register_function('bump', function(keys, args) return redis.call('INCRBY', keys[1], args[1]) end)"
"counters"
> FCALL bump 1 counter 2
(integer) 7
```

`redis.register_function{function_name=..., callback=..., flags={'no-writes'}}` declares a function that only reads, which [`FCALL_RO`](../commands/fcall_ro.md) can call. [`FUNCTION DUMP`](../commands/function-dump.md) and [`FUNCTION RESTORE`](../commands/function-restore.md) copy libraries between KiviDB servers; the format is not Redis's.

## Errors

`redis.call` raises the error of a command that fails, and the script stops with it; `redis.pcall` returns the error instead. Lua's `pcall` gives back the error's message, as in Redis:

```
> SET s abc
OK
> EVAL "local ok, e = pcall(redis.call, 'INCR', KEYS[1]) return e" 1 s
"ERR value is not an integer or out of range"
```

Around `error({err = ...})` or `error(redis.error_reply(...))`, `pcall` gives back the `err`. `assert` takes a string or a number as its message, and refuses a table: `bad argument #2 to 'assert' (string expected, got table)`.

Before 1.2, `pcall` gave back the raised table itself, and, for a command that failed, an error object whose text began `runtime error:` and ended in a traceback. A script that reads `e.err` from what `pcall` caught reads `e` now, and one that gives `assert` a table as its message fails.

## How scripts run

In Redis, one script runs at a time, and nothing else runs while it does. In KiviDB, with [`lua-parallel-scripts`](../reference/configuration.md#lua-parallel-scripts) (on by default), scripts whose keys all share a hash tag run alongside each other, each holding its tag:

- a script whose `KEYS` all have the same tag, `{queue:emails}:jobs` and `{queue:emails}:wait`, holds that tag while it runs. Scripts on other tags run at the same time; another on the same tag waits for it;
- such a script may use keys it did not name in `KEYS`, as BullMQ does, if they have the same tag. A key with another tag, or none, is refused:

```
> EVAL "return redis.call('SET', 'other', 1)" 1 {t}a
(error) ERR Script attempted to access the key 'other', which is outside the hash tag 't' of its KEYS (lua-parallel-scripts)
```

  and so are commands that look at every key, `KEYS`, `SCAN`, `DBSIZE`, `FLUSHALL`;
- a script with no keys, keys without a tag, or keys with different tags runs alone, as in Redis, and may use any key. So does every function called with `FCALL`, and a script the first time it runs, or one that takes more than 5 milliseconds.

Either way, a script is one step: no other command sees it half done. A script that names keys by a tag but uses keys outside it, and worked on Redis, has to name them, put them under the tag, or run with `lua-parallel-scripts no`.

## Long scripts

While a script runs, the clients waiting for it wait. After [`busy-reply-threshold`](../reference/configuration.md#busy-reply-threshold) milliseconds (5000), they are answered `BUSY`, and [`SCRIPT KILL`](../commands/script-kill.md), or [`FUNCTION KILL`](../commands/function-kill.md), can stop a script that has not written yet. One that has written cannot be stopped without losing the step: `SCRIPT KILL` replies `UNKILLABLE`, and only `SHUTDOWN NOSAVE` ends it. Before 1.2, `SCRIPT KILL` replied `OK` to such a script, which ran on.

## Replication and persistence

A script is replicated, and written to the append-only file, as the writes it made, not as the script: a script that uses `TIME` or `SRANDMEMBER` gives the same result on the replicas. The clock stands still while a script runs.

The writes of a script that writes more than once go to the replicas and the append-only file between a `MULTI` and an `EXEC`, as in Redis: a replica applies them together, with none of its own clients' commands in between, and a restart drops a script whose `EXEC` did not reach the file. One that writes once is sent as that one write. Before 1.2, the writes went one by one, and a client reading from a replica could see a script half done. A 1.1 replica of a 1.2 master still applies them, but logs `ERR unknown command 'MULTI'` for each: upgrade the replicas first.

`redis.replicate_commands()`, which many scripts written for Redis before 7 call first, returns true and changes nothing, as in Redis 7. `redis.set_repl(redis.REPL_ALL)` is taken; any other mode is refused. Before 1.2, neither function existed, and a script that called one failed.

On a replica, a script runs as long as it only reads, as in Redis; a write it makes is refused:

```
replica> EVAL "return redis.call('GET', KEYS[1])" 1 counter
"7"
replica> EVAL "return redis.call('INCR', KEYS[1])" 1 counter
(error) READONLY You can't write against a read only replica.
```

A script whose first line declares flags without `no-writes`, and a function registered without `no-writes`, are refused there before they run. Before 1.2, `EVAL`, `EVALSHA` and `FCALL` were refused on a replica even for a script that only read.

## In a cluster

The keys in `KEYS` must all be in the same slot, or the script gets `CROSSSLOT`; a cluster client sends it to the node that owns them.

A script uses only keys of one slot: that of its first key in `KEYS`, or, with none, of the first key it uses. Keep every key it uses in that slot, with a hash tag:

```
> EVAL "return redis.call('GET', 'user:2')" 1 user:1
(error) ERR Script attempted to access keys that do not hash to the same slot
```

A script flagged `allow-cross-slot-keys`, on its first line or as a function's flag, may use keys of other slots, as long as this node serves them. A key of a slot another node owns is refused either way: `ERR Script attempted to access a non local key in a cluster node`. Before 1.2, a script could write a key of a slot another node owns: the key was stored on this node, where clients would not find it.

## Commands a script cannot run

A script, or a function, cannot run the commands Redis 8.10 keeps from scripts: `SAVE`, `BGSAVE`, `BGREWRITEAOF`, `SHUTDOWN`, `CONFIG` (`GET` too), `ACL`, `CLIENT`, `MULTI`, `EXEC`, `WATCH`, the subscribe commands, `MONITOR`, `REPLICAOF`, `DEBUG`, `HELLO`, `EVAL` itself and a few others. `redis.call` of one raises the error, and the script stops; `redis.pcall` returns it:

```
> EVAL "return redis.call('BGSAVE')" 0
(error) ERR This Redis command is not allowed from script
> EVAL "return redis.call('CONFIG', 'GET', 'maxmemory')" 0
(error) ERR This Redis command is not allowed from script
```

Of `CLUSTER`, a script may run what only reads (`INFO`, `NODES`, `SLOTS`, `KEYSLOT`, ...), as in Redis, but not what changes the cluster, which Redis allows: moving a slot waits for the writes in flight, and the script would be one of them. `HOTKEYS HELP`, `BACKUP LIST` and `BACKUP STATUS` run from a script, as in Redis.

Before 1.2, a script could run all of these but `CLUSTER`, `HOTKEYS` and `BACKUP`, none of which it could run. A `SAVE` from a script on a replica could hang the replica.

## Differences from Redis

- Lua 5.4: integer division and the `//` operator, `utf8`, no `setfenv` or `getfenv`; `unpack` is still there. `bit`, `cjson`, `cmsgpack` and `struct` are there. Before 1.2, `struct` was not.
- `redis.set_repl()` takes only `redis.REPL_ALL`: a script cannot keep its writes from the replicas or the append-only file.
- `allow-stale` and `no-cluster` are accepted, and do nothing.
- [`SCRIPT DEBUG`](../commands/script-debug.md) replies `OK`: there is no debugger.
- Scripts run more slowly than in Redis: about a third of Redis's rate for small scripts, in the 1.1.0 measurement. A command does the same work faster where there is one.
