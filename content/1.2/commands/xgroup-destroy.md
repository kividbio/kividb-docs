---
title: "XGROUP DESTROY"
description: "Deletes the consumer group group of the stream at key, with its consumers and its pending entries list."
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
- `ERR The XGROUP subcommand requires the key to exist. Note that for CREATE you may want to use the MKSTREAM option to create an empty stream automatically.` if the key does not exist, as in Redis, since 1.2.1. 1.2.0 answered `0`.
- `WRONGTYPE` if the key holds another type.

## Examples

```
> XGROUP DESTROY jobs workers
(integer) 1
> XGROUP DESTROY jobs workers
(integer) 0
> XGROUP DESTROY nokey workers
(error) ERR The XGROUP subcommand requires the key to exist. Note that for CREATE you may want to use the MKSTREAM option to create an empty stream automatically.
```

With a consumer waiting:

```
client 1> XREADGROUP GROUP workers c BLOCK 0 STREAMS jobs >
client 2> XGROUP DESTROY jobs workers
(integer) 1
client 1> (error) NOGROUP No such key 'jobs' or consumer group 'workers' in XREADGROUP with GROUP option
```
