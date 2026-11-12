---
title: "DEBUG PROTOCOL"
description: "Replies with a value of the RESP type named: string, integer, double, bignum, null, array, set, map, attrib, push, verbatim, true or false."
version: "1.2"
command: "DEBUG PROTOCOL"
syntax: "DEBUG PROTOCOL type"
group: "server"
since: "1.2.1"
history: []
container: "DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
DEBUG PROTOCOL type
```

**Available since:** 1.2.1
<!-- generated: end -->
Replies with a value of the RESP type named: `string`, `integer`, `double`, `bignum`, `null`, `array`, `set`, `map`, `attrib`, `push`, `verbatim`, `true` or `false`. Use it to test how a client reads each type; the RESP3 types reach a RESP2 client in their RESP2 form.

`COMMAND` lists the `DEBUG` subcommands since 1.2.1, so each has a page; `DEBUG PROTOCOL` itself is older. See [`DEBUG`](debug.md).

## Reply

A value of that type, or an error for a type it does not know.

## Examples

With RESP3:

```
> DEBUG PROTOCOL double
(double) 3.141
> DEBUG PROTOCOL bignum
(big number) 1234567999999999999999999999999999999
> DEBUG PROTOCOL true
(true)
> DEBUG PROTOCOL foo
(error) Wrong protocol type name. Please use one of the following: string|integer|double|bignum|null|array|set|map|attrib|push|verbatim|true|false
```
