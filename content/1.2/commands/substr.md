---
title: "SUBSTR"
description: "Another name for GETRANGE, kept for old clients."
version: "1.2"
command: "SUBSTR"
syntax: "SUBSTR key start stop"
group: "string"
since: "1.1.0"
arity: 4
flags: ["readonly"]
acl_categories: ["read", "slow", "string"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SUBSTR key start stop
```

**Available since:** 1.1.0 · **ACL categories:** `@read`, `@slow`, `@string`
<!-- generated: end -->
Another name for [`GETRANGE`](getrange.md), kept for old clients.

## Examples

```
> SET k "hello world"
OK
> SUBSTR k 0 4
"hello"
```
