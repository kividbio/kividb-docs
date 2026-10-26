---
title: "ECHO"
description: "Returns message."
version: "1.2"
command: "ECHO"
syntax: "ECHO message"
group: "server"
since: "1.1.0"
arity: 2
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ECHO message
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Returns `message`.

## Examples

```
> ECHO hello
"hello"
```
