---
title: "EVALSHA"
description: "Runs a script the server already has, named by its SHA1 digest, as SCRIPT LOAD returns it, or as a previous EVAL cached it."
version: "1.2"
command: "EVALSHA"
syntax: "EVALSHA sha1 numkeys key [key ...] arg [arg ...]"
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
EVALSHA sha1 numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
Runs a script the server already has, named by its SHA1 digest, as [`SCRIPT LOAD`](script-load.md) returns it, or as a previous `EVAL` cached it. Clients send the digest instead of the whole script.

## Reply

- What the script returns, as for [`EVAL`](eval.md).
- `NOSCRIPT No matching script. Please use EVAL.` if the server does not have it, after a restart or `SCRIPT FLUSH`, for example.

## Examples

```
> SCRIPT LOAD "return ARGV[1]"
"098e0f0d1448c0a81dafe820f66d460eb09263da"
> EVALSHA 098e0f0d1448c0a81dafe820f66d460eb09263da 0 x
"x"
```
