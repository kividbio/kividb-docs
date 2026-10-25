---
title: "CLUSTER MEET"
description: "Initiate handshake with a peer."
version: "1.1"
command: "CLUSTER MEET"
syntax: "CLUSTER MEET ip port [cluster-bus-port]"
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
CLUSTER MEET ip port [cluster-bus-port]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Initiate handshake with a peer. Bus port defaults to `port + 10000`. A peer that cannot be reached leaves no entry behind.
