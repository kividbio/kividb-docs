---
title: "ASKING"
description: "Lets the connection's next command use a slot this node is importing (CLUSTER SETSLOT ... IMPORTING) but does not own yet."
version: "1.1"
command: "ASKING"
syntax: "ASKING"
group: "cluster"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["cluster", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ASKING
```

**Available since:** 1.1.0 · **ACL categories:** `@cluster`, `@fast`
<!-- generated: end -->
Lets the connection's next command use a slot this node is importing ([`CLUSTER SETSLOT ... IMPORTING`](cluster-setslot.md)) but does not own yet. A cluster client sends it before retrying a command answered with `ASK`. It applies to one command only.

## Examples

```
> SET k 1
(error) MOVED 7629 127.0.0.1:17652
> ASKING
OK
> SET k 1
OK
> GET k
(error) MOVED 7629 127.0.0.1:17652
```
