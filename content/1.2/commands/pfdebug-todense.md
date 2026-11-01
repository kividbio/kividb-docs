---
title: "PFDEBUG TODENSE"
description: "Converts a sparse HyperLogLog, one Redis wrote, to the dense encoding."
version: "1.2"
command: "PFDEBUG TODENSE"
syntax: "PFDEBUG TODENSE key"
group: "hyperloglog"
since: "1.1.0"
history: []
container: "PFDEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
PFDEBUG TODENSE key
```

**Available since:** 1.1.0
<!-- generated: end -->
Converts a sparse HyperLogLog, one Redis wrote, to the dense encoding. KiviDB writes only dense ones.

## Reply

- `1` if it was sparse and is now dense, `0` if it was dense already.

## Examples

```
> PFADD h a b c d
(integer) 1
> PFDEBUG TODENSE h
(integer) 0
```

Before 1.2, the reply was `OK`.
