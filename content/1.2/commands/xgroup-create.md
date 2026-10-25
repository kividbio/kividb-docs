---
title: "XGROUP CREATE"
description: "Creates the consumer group group on the stream at key, which will deliver entries after id: 0 for every entry, $ for only those added from now on."
version: "1.2"
command: "XGROUP CREATE"
syntax: "XGROUP CREATE key group id|$ [MKSTREAM] [ENTRIESREAD n]"
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
XGROUP CREATE key group id|$ [MKSTREAM] [ENTRIESREAD n]
```

**Available since:** 1.1.0
<!-- generated: end -->
Creates the consumer group `group` on the stream at `key`, which will deliver entries after `id`: `0` for every entry, `$` for only those added from now on. `MKSTREAM` creates an empty stream if the key does not exist. `ENTRIESREAD n` sets how many entries the group counts as read, for its lag.

## Reply

- `OK`.
- `BUSYGROUP Consumer Group name already exists`.
- `ERR The XGROUP subcommand requires the key to exist`, without `MKSTREAM`.

## Examples

```
> XADD jobs 1-0 task a
"1-0"
> XGROUP CREATE jobs workers 0
OK
> XGROUP CREATE jobs workers 0
(error) BUSYGROUP Consumer Group name already exists
> XGROUP CREATE nostream g $ MKSTREAM
OK
```
