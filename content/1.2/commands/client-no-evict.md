---
title: "CLIENT NO-EVICT"
description: "Accepted for compatibility, and changes nothing."
version: "1.2"
command: "CLIENT NO-EVICT"
syntax: "CLIENT NO-EVICT ON|OFF"
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
CLIENT NO-EVICT ON|OFF
```

**Available since:** 1.1.0
<!-- generated: end -->
Accepted for compatibility, and changes nothing. In Redis, `ON` exempts this connection from client eviction, which closes the connections using the most memory once all of them together pass `maxmemory-clients`. KiviDB has no client eviction: [`maxmemory-clients`](../reference/configuration.md) is accepted and has no effect, so no connection is closed to free memory, with or without this.

`ON` and `OFF` are the only arguments. Unlike Redis, `CLIENT LIST` shows no `e` flag for it.

## Reply

`OK`, or `ERR syntax error` for anything other than `ON` or `OFF`.

## Examples

```
> CLIENT NO-EVICT ON
OK
> CLIENT NO-EVICT maybe
(error) ERR syntax error
```
