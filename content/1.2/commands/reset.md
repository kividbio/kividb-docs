---
title: "RESET"
description: "Unsubscribe from everything and put the connection back as it was when it was opened: no transaction or watches, database 0, RESP2, no name, no tracking, and the default user if that needs no password"
version: "1.2"
command: "RESET"
syntax: "RESET"
group: "pub-sub"
since: "1.1.0"
arity: 1
flags: ["pubsub"]
acl_categories: ["connection", "pubsub", "slow"]
history: []
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
RESET
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@pubsub`, `@slow`
<!-- generated: end -->
## Description

Unsubscribe from everything and put the connection back as it was when it was opened: no transaction or watches, database 0, RESP2, no name, no tracking, and the `default` user if that needs no password
