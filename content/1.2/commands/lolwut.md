---
title: "LOLWUT"
description: "Returns a small drawing and the server's version."
version: "1.2"
command: "LOLWUT"
syntax: "LOLWUT [VERSION version]"
group: "server"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["server", "slow"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LOLWUT [VERSION version]
```

**Available since:** 1.1.0 · **ACL categories:** `@server`, `@slow`
<!-- generated: end -->
Returns the KiviDB logo, drawn in block characters, and a last line with the server's version and whether it is a 64-bit build. Redis draws a different piece of computer art for each major version, chosen with `VERSION`; KiviDB draws its logo whatever the arguments, so `VERSION` and any other argument are accepted and change nothing.

It touches no data. For the version in a form meant for programs, read `kividb_version` (and `redis_version`) from [`INFO server`](info.md).

## Reply

A bulk string.

## Examples

```
> LOLWUT
        ██╗  ██╗██╗         ██╗███████╗ ███████╗
        ...
        KiviDB version 1.2.0, bits 64
```
