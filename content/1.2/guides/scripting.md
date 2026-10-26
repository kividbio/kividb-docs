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
(error) ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.1.2-lua, or a kividb-lua release file)
```

Job queues that run on scripts, BullMQ and Sidekiq among them, need a build with Lua.

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

Scripts sent with `EVAL` or `SCRIPT LOAD` are kept, by their SHA1, until [`SCRIPT FLUSH`](../commands/script-flush.md), but not across a restart, and not on a replica that took its master's place: a client that gets `NOSCRIPT` from `EVALSHA` sends the script again with `EVAL`. Client libraries do that on their own.

### Known issue

Every distinct script sent with `EVAL` is kept until `SCRIPT FLUSH`, with no limit; Redis keeps at most 500 of them. Filed as [kividb#155](https://github.com/kividbio/kividb/issues/155).

## Functions

A library is loaded once, with a name, and kept: it is in the snapshot, it survives a restart, and it is copied to replicas.

```
> FUNCTION LOAD "#!lua name=counters\nredis.register_function('bump', function(keys, args) return redis.call('INCRBY', keys[1], args[1]) end)"
"counters"
> FCALL bump 1 counter 2
(integer) 7
```

`redis.register_function{function_name=..., callback=..., flags={'no-writes'}}` declares a function that only reads, which [`FCALL_RO`](../commands/fcall_ro.md) can call. [`FUNCTION DUMP`](../commands/function-dump.md) and [`FUNCTION RESTORE`](../commands/function-restore.md) copy libraries between KiviDB servers; the format is not Redis's.

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

While a script runs, the clients waiting for it wait. After [`busy-reply-threshold`](../reference/configuration.md#busy-reply-threshold) milliseconds (5000), they are answered `BUSY`, and [`SCRIPT KILL`](../commands/script-kill.md), or [`FUNCTION KILL`](../commands/function-kill.md), can stop a script that has not written yet. One that has written cannot be stopped without losing the step: only `SHUTDOWN NOSAVE` ends it.

### Known issue

`SCRIPT KILL` replies `OK` to a script that has already written, and the script runs on. Filed as [kividb#129](https://github.com/kividbio/kividb/issues/129).

## Replication and persistence

A script is replicated, and written to the append-only file, as the writes it made, not as the script: a script that uses `TIME` or `SRANDMEMBER` gives the same result on the replicas. The writes of one script go together. The clock stands still while a script runs.

## In a cluster

The keys in `KEYS` must all be in the same slot, or the script gets `CROSSSLOT`; a cluster client sends it to the node that owns them.

### Known issue

A script's `redis.call` on a key in another slot, which another node owns, is not refused: the key is written on this node, where clients will not find it. Keep every key a script uses in its slot, with a hash tag. Filed as [kividb#153](https://github.com/kividbio/kividb/issues/153).

## Differences from Redis

- Lua 5.4: integer division and the `//` operator, `utf8`, no `setfenv` or `getfenv`; `unpack` is still there. `bit` is there, `cjson` and `cmsgpack` too; `struct` is not.
- Lua's `pcall` around a `redis.call` that fails gives back the error's message, `ERR value is not an integer or out of range`, and `assert` takes only a string or a number as its message, as in Redis. Before 1.2, `pcall` gave back an error object whose text began `runtime error:` and ended in a traceback ([kividb#90](https://github.com/kividbio/kividb/issues/90)).
- `redis.log` does nothing: the line is not in the server's log.
- `redis.replicate_commands()` and `redis.set_repl()` do not exist: a script that starts with `redis.replicate_commands()`, as many written for Redis before 7 do, fails. Remove the line: scripts are always replicated as their writes. Filed, with `redis.log`, as [kividb#154](https://github.com/kividbio/kividb/issues/154).
- On a replica, `EVAL`, `EVALSHA` and `FCALL` are refused even for a script that only reads; use their `_RO` forms ([kividb#145](https://github.com/kividbio/kividb/issues/145)).
- `allow-stale`, `no-cluster` and `allow-cross-slot-keys` are accepted, and do nothing.
- [`SCRIPT DEBUG`](../commands/script-debug.md) replies `OK`: there is no debugger.
- Scripts run more slowly than in Redis: about a third of Redis's rate for small scripts, in the 1.1.0 measurement. A command does the same work faster where there is one.
