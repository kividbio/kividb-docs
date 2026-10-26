---
title: "FCALL_RO"
description: "FCALL for a function registered with the no-writes flag; any other is refused."
version: "1.1"
command: "FCALL_RO"
syntax: "FCALL_RO function_name numkeys key [key ...] arg [arg ...]"
group: "scripting"
since: "1.1.0"
arity: -3
flags: ["movablekeys", "readonly"]
acl_categories: ["scripting", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FCALL_RO function_name numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
[`FCALL`](fcall.md) for a function registered with the `no-writes` flag; any other is refused. It can be sent to a read-only replica.

## Examples

```
> FCALL_RO getk 1 greeting
"hi"
> FCALL_RO hello 0 x
(error) ERR Can not execute a script with write flag using *_ro command.
```
