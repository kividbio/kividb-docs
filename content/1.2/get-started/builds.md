---
title: "Choose a build"
description: "KiviDB 1.2 comes in four builds: the default one, and ones with Lua scripting, TLS, or both."
version: "1.2"
weight: 30
---

KiviDB is published in four builds. They are the same server; the others add Lua scripting, TLS, or both.

| Build | Adds | Docker tag | Binary file |
|---|---|---|---|
| default | | `v1.2.0-rc3` | `kividb-linux-x86_64.tar.gz` |
| `lua` | Lua scripting | `v1.2.0-rc3-lua` | `kividb-lua-linux-x86_64.tar.gz` |
| `tls` | TLS | `v1.2.0-rc3-tls` | `kividb-tls-linux-x86_64.tar.gz` |
| `full` | Lua scripting and TLS | `v1.2.0-rc3-full` | `kividb-full-linux-x86_64.tar.gz` |

The tags are those of the release candidate: see [Install KiviDB](install.md). The Linux packages (`.deb`, `.rpm`) are the default build.

## The default build

The default build has every command but the scripting ones. It is the build measured in KiviDB's benchmarks. Use it unless you need scripts or TLS.

In the default build, the scripting commands (`EVAL`, `EVALSHA`, `SCRIPT`, `FUNCTION`, `FCALL` and the rest) reply with an error that names the build to use instead:

```
> EVAL "return 1" 0
(error) ERR this build of KiviDB has no Lua: EVAL, SCRIPT, FUNCTION and FCALL need the lua or full variant (Docker image kividb/kividb:v1.2.0-rc3-lua, or a kividb-lua release file)
```

In 1.1 it said `Lua scripting is not supported by KiviDB`, which read as if no build had it.

## When you need Lua

Choose the `lua` or `full` build if you run scripts, or use a library that does. **BullMQ** (Node.js job queues) and **Sidekiq** (Ruby background jobs) both send Lua scripts, and need the `lua` or `full` build.

The builds with Lua also use [mimalloc](https://github.com/microsoft/mimalloc) as the memory allocator on Linux, where the others use the system's: scripts allocate and free many small blocks, often on different threads.

## When you need TLS

Choose the `tls` or `full` build to encrypt connections, between clients and the server, and between cluster nodes and replicas. A build without TLS does not start if it is given `--tls-port`, rather than serving unencrypted connections on it.

## Building it yourself

Each build is a set of Cargo features. See [Install KiviDB](install.md#from-source).

| Build | `cargo build --release` with |
|---|---|
| default | (no features) |
| `lua` | `--features lua` |
| `tls` | `--features tls` |
| `full` | `--features lua,tls` |
