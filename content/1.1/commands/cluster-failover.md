---
title: "CLUSTER FAILOVER"
description: "Sent to a replica: makes it the master of its shard, and its master a replica of it."
version: "1.1"
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
| none | The master pauses writes, the replica catches up, and then it is elected. Nothing acknowledged is lost. |
| `FORCE` | Skips the catching up, for a master that cannot be reached. An election is still held. |
| `TAKEOVER` | Skips the election too: the replica takes the slots at once, without the other masters' agreement. For when no majority of masters can be reached. |

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
