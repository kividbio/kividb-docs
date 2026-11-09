---
title: "XGROUP CREATECONSUMER"
description: "Creates the consumer consumer in the group."
version: "1.2"
command: "XGROUP CREATECONSUMER"
syntax: "XGROUP CREATECONSUMER key group consumer"
group: "stream"
since: "1.1.0"
history: []
container: "XGROUP"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
XGROUP CREATECONSUMER key group consumer
```

**Available since:** 1.1.0
<!-- generated: end -->
Creates the consumer `consumer` in the consumer group `group` of the stream at `key`. You rarely need it: [`XREADGROUP`](xreadgroup.md) creates a consumer the first time it reads with that name. Creating one in advance makes it show in [`XINFO CONSUMERS`](xinfo-consumers.md) before it has read anything, where its `inactive` time is `-1` until it is first handed entries.

## Reply

- `1` if the consumer was created, `0` if the group already had it.

## Errors

- `NOGROUP No such consumer group '<group>' for key name '<key>'` if the group does not exist.
- `ERR no such key` if the key does not exist. Redis answers `ERR The XGROUP subcommand requires the key to exist` instead.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> XGROUP CREATECONSUMER jobs workers dave
(integer) 1
> XGROUP CREATECONSUMER jobs workers dave
(integer) 0
> XINFO CONSUMERS jobs workers
...
3) 1) "name"
   2) "dave"
   3) "pending"
   4) (integer) 0
   5) "idle"
   6) (integer) 4
   7) "inactive"
   8) (integer) -1
> XGROUP CREATECONSUMER jobs nogroup dave
(error) NOGROUP No such consumer group 'nogroup' for key name 'jobs'
> XGROUP CREATECONSUMER nokey workers dave
(error) ERR no such key
```
