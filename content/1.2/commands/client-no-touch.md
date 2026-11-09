---
title: "CLIENT NO-TOUCH"
description: "Accepted."
version: "1.2"
command: "CLIENT NO-TOUCH"
syntax: "CLIENT NO-TOUCH ON|OFF"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLIENT NO-TOUCH ON|OFF
```

**Available since:** 1.1.0
<!-- generated: end -->
Accepted for compatibility, and changes nothing. In Redis it stops this connection's commands updating keys' last access time, so that a monitoring or backup tool reading every key does not make them all look recently used to LRU and LFU eviction. KiviDB records access times only while an LRU or LFU [`maxmemory-policy`](../reference/configuration.md#maxmemory-policy) is selected, and not per client.

`ON` and `OFF` are the only arguments. Unlike Redis, `CLIENT LIST` shows no `T` flag for it.

## Reply

`OK`, or `ERR syntax error` for anything other than `ON` or `OFF`.

## Examples

```
> CLIENT NO-TOUCH ON
OK
> CLIENT NO-TOUCH x
(error) ERR syntax error
```
