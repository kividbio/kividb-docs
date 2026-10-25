---
title: "BRPOPLPUSH"
description: "RPOPLPUSH that waits until source has an element or timeout seconds have passed."
version: "1.1"
command: "BRPOPLPUSH"
syntax: "BRPOPLPUSH source destination timeout"
group: "list"
since: "1.1.0"
arity: 4
flags: ["blocking", "write"]
acl_categories: ["blocking", "list", "slow", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
BRPOPLPUSH source destination timeout
```

**Available since:** 1.1.0 · **ACL categories:** `@blocking`, `@list`, `@slow`, `@write`
<!-- generated: end -->
[`RPOPLPUSH`](rpoplpush.md) that waits until `source` has an element or `timeout` seconds have passed. Use [`BLMOVE`](blmove.md) in new code.

## Reply

- The element moved, or `nil` if the timeout passed.

## Examples

```
> BRPOPLPUSH empty dst 0.1
(nil)
```
