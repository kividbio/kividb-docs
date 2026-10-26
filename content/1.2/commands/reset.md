---
title: "RESET"
description: "Puts the connection back as it was when it was opened: unsubscribed from everything, out of any transaction and with no keys watched, on database 0, speaking RESP2, with no name and no client-side ca…"
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
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
RESET
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@pubsub`, `@slow`
<!-- generated: end -->
Puts the connection back as it was when it was opened: unsubscribed from everything, out of any transaction and with no keys watched, on database 0, speaking RESP2, with no name and no client-side caching, and authenticated as the `default` user if that user needs no password.

## Reply

- `RESET`.

## Examples

```
> RESET
RESET
```
