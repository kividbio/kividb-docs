---
title: "CLIENT REPLY"
description: "OFF stops replies on this connection until ON; SKIP drops the reply to the next command."
version: "1.2"
command: "CLIENT REPLY"
syntax: "CLIENT REPLY ON|OFF|SKIP"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLIENT REPLY ON|OFF|SKIP
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

`OFF` stops replies on this connection until `ON`; `SKIP` drops the reply to the next command. Messages — Pub/Sub, RESP3 pushes — are still sent
