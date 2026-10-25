---
title: "EVAL_RO"
description: "EVAL for a script that only reads: a command in it that writes fails."
version: "1.2"
command: "EVAL_RO"
syntax: "EVAL_RO script numkeys key [key ...] arg [arg ...]"
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
EVAL_RO script numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
[`EVAL`](eval.md) for a script that only reads: a command in it that writes fails. It can be sent to a read-only replica.

## Examples

```
> EVAL_RO "return redis.call('GET', KEYS[1])" 1 greeting
"hi"
> EVAL_RO "return redis.call('SET', KEYS[1], 1)" 1 greeting
(error) ERR Write commands are not allowed from read-only scripts. script: 492690f94c6c4d47fbb6eb03029dcdfcf5a17028, on @user_script:1.
```
