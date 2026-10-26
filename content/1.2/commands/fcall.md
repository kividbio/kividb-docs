---
title: "FCALL"
description: "Calls a function of a library loaded with FUNCTION LOAD."
version: "1.2"
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

## Known issue

Refused on a replica with `READONLY`, even for a function that only reads; use [`FCALL_RO`](fcall_ro.md) there. Filed as [kividb#145](https://github.com/kividbio/kividb/issues/145).

In a cluster, a `redis.call` on a key in a slot another node owns is not refused: the key is written on this node, where clients will not find it. Filed as [kividb#153](https://github.com/kividbio/kividb/issues/153).

## Reply

- What the function returns, converted as for [`EVAL`](eval.md).
- `ERR Function not found`.

## Examples

```
> FCALL hello 0 Ada
"hi Ada"
```
