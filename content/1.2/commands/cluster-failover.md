---
title: "CLUSTER FAILOVER"
description: "Sent to a replica: makes it the master of its shard, and its master a replica of it."
version: "1.2"
command: "CLUSTER FAILOVER"
syntax: "CLUSTER FAILOVER [FORCE | TAKEOVER]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER FAILOVER [FORCE | TAKEOVER]
```

**Available since:** 1.1.0
<!-- generated: end -->
Sent to a replica: makes it the master of its shard, and its master a replica of it.

| Option | Effect |
|---|---|
| none | The master pauses writes, the replica catches up, and then it is elected. Nothing acknowledged is lost. The master holds writes for up to 10 seconds, and the replica has 5 to catch up and win, as in Redis; otherwise it gives the failover up (`Manual failover abandoned` in its log), and the master goes on. Before 1.2, the pause was 5 seconds, and a replica that won later still took over, losing the writes acknowledged meanwhile. |
| `FORCE` | Skips the catching up, for a master that cannot be reached. An election is still held. |
| `TAKEOVER` | Skips the election too: the replica takes the slots at once, without the other masters' agreement. For when no majority of masters can be reached. |

During an atomic slot migration's handover from this replica's master ([`CLUSTER MIGRATION`](cluster-migration.md)), and for 3 seconds after it, a failover without `TAKEOVER` does not happen: the replica still replies `OK`, and it and its master log why (`Manual failover requested by ... refused`). Ask again a few seconds later. That is since 1.2.1, so that a failover and a handover exclude each other: in 1.2.0, a failover of the source while `CLUSTER MIGRATION IMPORT` ran lost the writes the new master acknowledged to the moving slots. `TAKEOVER`, which asks no other node, is not held back.

A master that fails is replaced the same way without this command: once a majority of masters have not heard from it for `cluster-node-timeout` milliseconds, its replicas stand for election. When it comes back, it finds its slots taken at a higher epoch and becomes a replica.

## Reply

- `OK`, before the failover is done.
- `ERR You should send CLUSTER FAILOVER to a replica`.

## Examples

```
> CLUSTER FAILOVER
OK
> ROLE
1) "master"
...
```
