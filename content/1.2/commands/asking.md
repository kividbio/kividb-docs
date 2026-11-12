---
title: "ASKING"
description: "Lets the connection's next command use a slot this node is importing (CLUSTER SETSLOT ... IMPORTING) but does not own yet."
version: "1.2"
command: "ASKING"
syntax: "ASKING"
group: "cluster"
since: "1.1.0"
arity: 1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: [{"release": "1.2.1", "change": "acl categories: added connection; removed cluster"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ASKING
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`

**History:**

- 1.2.1: acl categories: added connection; removed cluster
<!-- generated: end -->
Lets the connection's next command use a slot this node is importing ([`CLUSTER SETSLOT ... IMPORTING`](cluster-setslot.md)) but does not own yet. A cluster client sends it before retrying a command answered with `ASK`. It applies to one command only.

On a server that is not a cluster node it is refused with `ERR This instance has cluster support disabled`, as in Redis, since 1.2.1; before, it answered `OK`.

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
