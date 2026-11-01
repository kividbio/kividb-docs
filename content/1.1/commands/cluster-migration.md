---
title: "CLUSTER MIGRATION"
description: "Moves whole slot ranges to this node from the master that owns them, in the background: Redis 8.4's atomic slot migration."
version: "1.1"
command: "CLUSTER MIGRATION"
syntax: "CLUSTER MIGRATION IMPORT start-slot end-slot [start-slot end-slot ...]\nCLUSTER MIGRATION STATUS [ID task-id | ALL]\nCLUSTER MIGRATION CANCEL <ID task-id | ALL>"
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
CLUSTER MIGRATION IMPORT start-slot end-slot [start-slot end-slot ...]
CLUSTER MIGRATION STATUS [ID task-id | ALL]
CLUSTER MIGRATION CANCEL <ID task-id | ALL>
```

**Available since:** 1.1.0
<!-- generated: end -->
Moves whole slot ranges to this node from the master that owns them, in the background: Redis 8.4's atomic slot migration. Run on the node that is to receive them.

| Form | Effect |
|---|---|
| `IMPORT start-slot end-slot ...` | Starts a task for the ranges, which must all belong to one other master. Returns the task's ID at once. |
| `STATUS [ID task-id \| ALL]` | The tasks this node knows of, as destination (`operation` `import`) or source (`migrate`). |
| `CANCEL <ID task-id \| ALL>` | Cancels them, and returns how many. The source keeps the slots and the destination drops what it had received. |

The source sends a snapshot of the slots' keys, then the writes that arrive for them meanwhile. When the destination is less than `cluster-slot-migration-handoff-max-lag-bytes` behind, the source pauses writes, sends the rest, and the destination takes the slots. Clients get no `ASK` and no `TRYAGAIN`; only, at the end, the `MOVED` that says where the slots are now. No acknowledged write is lost or applied twice, but for the known issue below.

During the handoff every write to the source waits, not only those for the slots that move: `write_pause_ms` in `STATUS` says how long. If the pause would last longer than `cluster-slot-migration-write-pause-timeout`, the attempt is abandoned and tried again; in 1.1, writes can then be lost, as the known issue below says.

## Known issue

In 1.1, the pause at the handoff ends by itself after `cluster-slot-migration-write-pause-timeout`, 10 seconds by default, whether or not the handoff has finished. If sending the last writes and the destination's taking the slots last longer than that, because the destination's disk or the network is slow, or because the destination's answer is lost, the source takes writes for the moving slots again and no longer sends them on. When the destination then takes the slots, the source deletes its copy of their keys, and those writes are lost, although their clients got `OK`.

A higher [`cluster-slot-migration-write-pause-timeout`](../reference/configuration.md#cluster-slot-migration-write-pause-timeout), set on the command line or in the configuration file, makes it less likely, at the cost of a longer wait for every write to the source when a handoff is slow; it does not rule it out. Move slots while the destination's disk and the network between the two nodes are not under heavy load.

In 1.2.0, writes stay paused until the source knows whether the destination took the slots. Filed as [kividb#278](https://github.com/kividbio/kividb/issues/278), fixed in 1.2.0 by [kividb#279](https://github.com/kividbio/kividb/pull/279).

## Reply

- `IMPORT`: the task ID; `ERR I already own slot slot`.
- `STATUS`: per task, `id`, `slots`, `source`, `dest`, `operation`, `state` (`in_progress`, `completed`, `failed` or `canceled`), `last_error`, `retries`, `create_time`, `start_time`, `end_time`, `write_pause_ms` and `capture_pause_ms`.
- `CANCEL`: the number of tasks cancelled.

## Examples

```
> CLUSTER MIGRATION IMPORT 8192 8291
"87cf25c0e5b2e4c8819830e481a53825c07f6e48"
> CLUSTER MIGRATION STATUS
1)  1) "id"
    2) "87cf25c0e5b2e4c8819830e481a53825c07f6e48"
    3) "slots"
    4) "8192-8291"
    5) "source"
    6) "2e3eefa800e802047f92cb529ac5d1424daebb27"
    7) "dest"
    8) "b2744aeada9b56dd000f101f31447a33a15c9b08"
    9) "operation"
   10) "import"
   11) "state"
   12) "completed"
   ...
```
