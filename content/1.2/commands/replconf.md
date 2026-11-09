---
title: "REPLCONF"
description: "Sent by a replica to its master during replication, and not meant for applications."
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
Sent by a replica to its master during replication, and not meant for applications. A replica sends it before [`PSYNC`](psync.md) to give the port it listens on (`listening-port`) and what it can do (`capa`), then to acknowledge how far it has applied the master's stream (`ACK offset`): at once after applying commands, and about once a second when idle. [`WAIT`](wait.md) counts these acknowledgements. A KiviDB master does not send `GETACK`.

[Replication](../guides/replication.md) describes the whole exchange.

## Reply

`OK`. On the replication link, `ACK` is read without a reply.

## Examples

```
> REPLCONF listening-port 6381
OK
> REPLCONF capa eof capa psync2
OK
```
