---
title: "CLIENT NO-TOUCH"
description: "Accepted."
version: "1.2"
command: "CLIENT NO-TOUCH"
syntax: "CLIENT NO-TOUCH ON|OFF"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT NO-TOUCH ON|OFF
```

**Available since:** 1.1.0
<!-- generated: end -->
Accepted. In Redis it stops this connection's commands updating keys' last access time. KiviDB records access times only while an LRU or LFU `maxmemory-policy` is selected, and not per client, so it changes nothing.
