---
title: "QUIT"
description: "Asks the server to close the connection, after replying OK."
version: "1.2"
command: "QUIT"
syntax: "QUIT"
group: "pub-sub"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["connection", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
QUIT
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@slow`
<!-- generated: end -->
Asks the server to close the connection, after replying `OK`. Clients usually close it themselves instead.
