---
title: "CONFIG REWRITE"
description: "Writes the current settings to the configuration file the server was started with, /etc/kividb/kividb.conf by default, creating it and its directory if needed."
version: "1.1"
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
Writes the current settings to the configuration file the server was started with, `/etc/kividb/kividb.conf` by default, creating it and its directory if needed. The file is replaced in one step, through a temporary file, and keeps its mode and, when run as root, its owner; a new file is made `0600`. Redis resets the mode to `0644`, less the umask, instead.

## Examples

```
> CONFIG SET maxmemory 2mb
OK
> CONFIG REWRITE
OK
```
