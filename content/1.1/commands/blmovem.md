---
title: "BLMOVEM"
description: "LMOVEM that waits until source has an element, or, with EXACTLY, enough of them, or until timeout seconds have passed."
version: "1.1"
command: "BLMOVEM"
syntax: "BLMOVEM source destination LEFT|RIGHT LEFT|RIGHT timeout [<COUNT count | EXACTLY count> <OBO | BULK>]"
group: "list"
since: "1.1.0"
arity: -2
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BLMOVEM source destination LEFT|RIGHT LEFT|RIGHT timeout [<COUNT count | EXACTLY count> <OBO | BULK>]
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
[`LMOVEM`](lmovem.md) that waits until `source` has an element, or, with `EXACTLY`, enough of them, or until `timeout` seconds have passed.

## Reply

- An array of the elements moved.
- `nil` if the timeout passed.

## Examples

```
> BLMOVEM empty dst LEFT RIGHT 0.1
(nil)
```
