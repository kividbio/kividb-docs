---
title: "XGROUP HELP"
description: "In Redis, XGROUP HELP lists the XGROUP subcommands with a line on what each does."
version: "1.2"
command: "XGROUP HELP"
syntax: "XGROUP HELP"
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
XGROUP HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
In Redis, `XGROUP HELP` lists the [`XGROUP`](xgroup.md) subcommands with a line on what each does. KiviDB 1.2.0 does not implement it: it answers `ERR unknown subcommand for XGROUP`, although [`COMMAND DOCS`](command-docs.md) lists `xgroup|help`. A client that sends it to discover the subcommands gets the error, and should not rely on it.

The subcommands are [`XGROUP CREATE`](xgroup-create.md), [`XGROUP CREATECONSUMER`](xgroup-createconsumer.md), [`XGROUP DELCONSUMER`](xgroup-delconsumer.md), [`XGROUP DESTROY`](xgroup-destroy.md) and [`XGROUP SETID`](xgroup-setid.md); each has its own page here.

## Reply

- In 1.2.0, the error `ERR unknown subcommand for XGROUP`.

## Examples

```
> XGROUP HELP
(error) ERR unknown subcommand for XGROUP
```
