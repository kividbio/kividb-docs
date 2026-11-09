---
title: "XGROUP DESTROY"
description: "Deletes the group, its consumers and its pending entries."
version: "1.2"
command: "XGROUP DESTROY"
syntax: "XGROUP DESTROY key group"
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
XGROUP DESTROY key group
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes the consumer group `group` of the stream at `key`, with its consumers and its pending entries list. The stream and its entries are not touched, nor are its other groups. Use it when a group's readers are retired for good; to have a group read the stream again from the start, [`XGROUP SETID`](xgroup-setid.md) keeps it and its consumers.

A client blocked in [`XREADGROUP`](xreadgroup.md) on the group is woken with an error: `NOGROUP No such key '<key>' or consumer group '<group>' in XREADGROUP with GROUP option`.

## Reply

- `1` if the group existed and was deleted, `0` if not.
- `0` also when the key does not exist, where Redis answers `ERR The XGROUP subcommand requires the key to exist`.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> XGROUP DESTROY jobs workers
(integer) 1
> XGROUP DESTROY jobs workers
(integer) 0
> XGROUP DESTROY nokey workers
(integer) 0
```

With a consumer waiting:

```
client 1> XREADGROUP GROUP workers c BLOCK 0 STREAMS jobs >
client 2> XGROUP DESTROY jobs workers
(integer) 1
client 1> (error) NOGROUP No such key 'jobs' or consumer group 'workers' in XREADGROUP with GROUP option
```
