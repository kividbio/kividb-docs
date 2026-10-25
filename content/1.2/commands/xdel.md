---
title: "XDEL"
description: "Deletes entries from the stream at key by ID."
version: "1.2"
command: "XDEL"
syntax: "XDEL key id [id ...]"
group: "stream"
since: "1.1.0"
arity: -3
flags: ["write"]
acl_categories: ["slow", "stream", "write"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XDEL key id [id ...]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`, `@stream`, `@write`
<!-- generated: end -->
Deletes entries from the stream at `key` by ID. The stream keeps its last ID, so new entries still get greater ones.

## Reply

- The number of entries deleted.

## Examples

```
> XADD s 1-1 temp 20
"1-1"
> XDEL s 1-1 9-9
(integer) 1
```
