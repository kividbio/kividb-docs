---
title: "CONFIG SET"
description: "All or nothing: an unknown parameter, a value out of range, a parameter that cannot change at run time or one named twice is an error naming it, and none of the pairs is applied."
version: "1.1"
command: "CONFIG SET"
syntax: "CONFIG SET param value [param value ...]"
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
CONFIG SET param value [param value ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

All or nothing: an unknown parameter, a value out of range, a parameter that cannot change at run time or one named twice is an error naming it, and none of the pairs is applied. `requirepass`, `slowlog-log-slower-than`, `slowlog-max-len`, `maxmemory`, `maxmemory-policy`, `maxmemory-samples`, `lfu-log-factor`, `lfu-decay-time`, `appendonly`, `loglevel`, `repl-backlog-size`, `repl-backlog-ttl`, `repl-diskless-load` all apply immediately at runtime without restart
