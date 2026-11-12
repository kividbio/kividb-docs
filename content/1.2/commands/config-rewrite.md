---
title: "CONFIG REWRITE"
description: "Writes the current settings to the configuration file the server was started with, /etc/kividb/kividb.conf by default."
version: "1.2"
command: "CONFIG REWRITE"
syntax: "CONFIG REWRITE"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CONFIG REWRITE
```

**Available since:** 1.1.0
<!-- generated: end -->
Writes the current settings to the configuration file the server was started with, `/etc/kividb/kividb.conf` by default. The file is replaced in one step, through a temporary file, and keeps its mode and, when run as root, its owner. Redis resets the mode to `0644`, less the umask, instead.

A server that was started without a configuration file (the file given by `--configfile`, or the default one, was not there) replies `ERR The server is running without a config file` and writes nothing, as Redis does; `config_file` in `INFO server` is then empty. A file that exists, even an empty one, is rewritten. The packages start the server from `/etc/kividb/kividb.conf`; the Docker image starts it without a file, so to use `CONFIG REWRITE` there, mount one and start the server with `--configfile` pointing at it.

That is since 1.2.1. 1.2.0 created the file, and its directory, when the server had been started without one, with `port`, `replicaof` and every other setting in it, and the next server started on the host without a file of its own loaded it. Redis Sentinel sends `REPLICAOF` and then `CONFIG REWRITE` to the replicas it reconfigures, so unrelated servers could become replicas this way. On a host where an earlier release made `/etc/kividb/kividb.conf` so, look for a `replicaof` line nobody wrote in it, and delete or fix it.

## Examples

On a server started with `--configfile /etc/kividb/kividb.conf`, a file that exists:

```
> CONFIG SET maxmemory 2mb
OK
> CONFIG REWRITE
OK
```

On a server started without one:

```
> CONFIG REWRITE
(error) ERR The server is running without a config file
```
