---
title: "CLIENT SETINFO"
description: "Records the client library's name, LIB-NAME, or version, LIB-VER, on the connection; CLIENT LIST and CLIENT INFO show them as lib-name and lib-ver."
version: "1.2"
command: "CLIENT SETINFO"
syntax: "CLIENT SETINFO LIB-NAME name | LIB-VER ver"
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
CLIENT SETINFO LIB-NAME name | LIB-VER ver
```

**Available since:** 1.1.0
<!-- generated: end -->
Records the client library's name, `LIB-NAME`, or version, `LIB-VER`, on the connection; [`CLIENT LIST`](client-list.md) and [`CLIENT INFO`](client-info.md) show them as `lib-name` and `lib-ver`. Client libraries send it when they connect, so that a server's operator can see which libraries, and which versions, are connected. One call sets one of the two; send it twice to set both.

A value cannot contain spaces, newlines or other special characters, since `CLIENT LIST` separates its fields with spaces.

## Reply

`OK`, or an error.

## Errors

- `ERR lib-name cannot contain spaces, newlines or special characters.` (or `lib-ver`).
- `ERR Unrecognized option 'FOO'` for an option other than the two.

## Examples

```
> CLIENT SETINFO LIB-NAME redis-py
OK
> CLIENT SETINFO LIB-VER 5.0.1
OK
> CLIENT SETINFO LIB-NAME "a b"
(error) ERR lib-name cannot contain spaces, newlines or special characters.
```
