---
title: "REPLCONF"
description: "Sent between a master and its replicas during replication: the replica's port, its acknowledged offset, and its capabilities."
version: "1.2"
command: "REPLCONF"
syntax: "REPLCONF ..."
group: "server"
since: "1.1.0"
arity: -1
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
REPLCONF ...
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`
<!-- generated: end -->
Sent between a master and its replicas during replication, and not meant for applications. A replica sends it before [`PSYNC`](psync.md) to give the port it listens on (`listening-port`) and what it can do (`capa`), then about once a second to acknowledge how far it has applied the master's stream (`ACK offset`). The master sends `GETACK *` to ask its replicas for an acknowledgement, which [`WAIT`](wait.md) relies on.

[Replication](../guides/replication.md) describes the whole exchange.

## Reply

`OK` to most options; `ACK` gets no reply.

## Examples

```
> REPLCONF listening-port 6381
OK
> REPLCONF capa eof capa psync2
OK
```
