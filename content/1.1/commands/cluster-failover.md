---
title: "CLUSTER FAILOVER"
description: "Manually promote this replica."
version: "1.1"
command: "CLUSTER FAILOVER"
syntax: "CLUSTER FAILOVER [FORCE | TAKEOVER]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLUSTER FAILOVER [FORCE | TAKEOVER]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Manually promote this replica. By default the master pauses writes and the replica catches up before it stands for election, so nothing acknowledged is lost. `FORCE` skips that handshake (the master may be unreachable) but still wins an election; `TAKEOVER` skips the election too (dangerous).
