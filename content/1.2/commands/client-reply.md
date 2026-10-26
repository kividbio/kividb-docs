---
title: "CLIENT REPLY"
description: "OFF stops the replies to this connection's commands until ON; SKIP drops the reply to the next command alone."
version: "1.2"
command: "CLIENT REPLY"
syntax: "CLIENT REPLY ON|OFF|SKIP"
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
CLIENT REPLY ON|OFF|SKIP
```

**Available since:** 1.1.0
<!-- generated: end -->
`OFF` stops the replies to this connection's commands until `ON`; `SKIP` drops the reply to the next command alone. Pub/sub messages and RESP3 push messages are still sent.
