---
title: "FCALL"
description: "Calls a function of a library loaded with FUNCTION LOAD."
version: "1.1"
command: "FCALL"
syntax: "FCALL function_name numkeys key [key ...] arg [arg ...]"
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
FCALL function_name numkeys key [key ...] arg [arg ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@scripting`, `@slow`
<!-- generated: end -->
Calls a function of a library loaded with [`FUNCTION LOAD`](function-load.md). `numkeys` is how many of the arguments that follow are key names, passed to the function as its first argument; the rest are its second.

A function is held to the flags it was registered with. With `no-writes`, it cannot write. When the server is at its memory limit, a function runs only if it has `allow-oom` or `no-writes`.

## Reply

- What the function returns, converted as for [`EVAL`](eval.md).
- `ERR Function not found`.

## Examples

```
> FCALL hello 0 Ada
"hi Ada"
```
