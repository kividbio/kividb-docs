---
title: "CONFIG REWRITE"
description: "Persist the current runtime config to the file the server was started with (default /etc/kividb/kividb.conf)."
version: "1.1"
command: "CONFIG REWRITE"
syntax: "CONFIG REWRITE"
group: "server"
since: "1.1.0"
history: []
container: "CONFIG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CONFIG REWRITE
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Persist the current runtime config to the file the server was started with (default `/etc/kividb/kividb.conf`). Creates the file and parent directories if they don't exist. Atomic write via tmpfile-rename. Keeps the file's mode, and its owner when run as root; a new file is `0600`. Redis resets the mode to `0644` less the umask instead
