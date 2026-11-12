---
title: "LOLWUT"
description: "Returns the KiviDB logo, drawn in block characters, and a last line with the server's version, KiviDB version 1.2.1, bits 64."
version: "1.2"
command: "LOLWUT"
syntax: "LOLWUT [VERSION version]"
group: "server"
since: "1.1.0"
arity: -1
flags: []
acl_categories: ["slow"]
history: [{"release": "1.2.1", "change": "acl categories: removed server"}]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
LOLWUT [VERSION version]
```

**Available since:** 1.1.0 · **ACL categories:** `@slow`

**History:**

- 1.2.1: acl categories: removed server
<!-- generated: end -->
Returns the KiviDB logo, drawn in block characters, and a last line with the server's version, `KiviDB version 1.2.1, bits 64`. Redis draws a different piece of computer art for each major version, chosen with `VERSION`; KiviDB draws its logo whatever the version. `VERSION` takes an integer, as do the options Redis's versions 5 and 6 take, and anything else is `ERR value is not an integer or out of range`, as in Redis, since 1.2.1; 1.2.0 accepted any argument.

It touches no data. For the version in a form meant for programs, read `kividb_version` (and `redis_version`) from [`INFO server`](info.md).

## Reply

A bulk string.

## Examples

```
> LOLWUT
        ██╗  ██╗██╗         ██╗███████╗ ███████╗
        ...
        KiviDB version 1.2.1, bits 64
```
