---
title: "CLUSTER SETSLOT"
description: "Sets the state of one slot on this node, for moving it by hand."
version: "1.1"
command: "CLUSTER SETSLOT"
syntax: "CLUSTER SETSLOT slot <IMPORTING|MIGRATING|NODE> node-id\nCLUSTER SETSLOT slot STABLE"
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
CLUSTER SETSLOT slot <IMPORTING|MIGRATING|NODE> node-id
CLUSTER SETSLOT slot STABLE
```

**Available since:** 1.1.0
<!-- generated: end -->
Sets the state of one slot on this node, for moving it by hand.

| Form | Effect |
|---|---|
| `IMPORTING node-id` | On the destination: the slot is coming from `node-id`. Commands for it are served after [`ASKING`](asking.md). |
| `MIGRATING node-id` | On the source: the slot is going to `node-id`. A command for a key that has already left is answered with `ASK slot host:port`. |
| `NODE node-id` | `node-id` owns the slot now. Sent to the destination, then to the source. |
| `STABLE` | Clears `IMPORTING` or `MIGRATING`. |

Moving a slot by hand takes four steps, which `redis-cli --cluster reshard` drives:

1. `CLUSTER SETSLOT slot IMPORTING source-id` on the destination;
2. `CLUSTER SETSLOT slot MIGRATING destination-id` on the source;
3. [`MIGRATE`](migrate.md) the slot's keys, in batches, from the source;
4. `CLUSTER SETSLOT slot NODE destination-id` on the destination, then on the source.

A multi-key command whose keys are partly on each side meanwhile is answered with `TRYAGAIN`. [`CLUSTER MIGRATION`](cluster-migration.md) moves slots in one command, without `ASK`.

A node that loses a slot to another master, by `SETSLOT ... NODE` or on the losing side of a partition, deletes the keys it holds in that slot.

## Reply

- `OK`.
- `ERR Unknown node`.
- `ERR Unknown SETSLOT subcommand 'name'`.

## Examples

```
> CLUSTER SETSLOT 2780 IMPORTING b2744aeada9b56dd000f101f31447a33a15c9b08
OK
```

On the source, once the key has gone:

```
> GET user:7
(error) ASK 2780 127.0.0.1:17622
```
