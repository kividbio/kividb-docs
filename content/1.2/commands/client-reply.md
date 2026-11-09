---
title: "CLIENT REPLY"
description: "OFF stops the replies to this connection's commands until ON; SKIP drops the reply to the next command alone."
version: "1.2"
command: "CLIENT REPLY"
syntax: "CLIENT REPLY ON|OFF|SKIP"
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
CLIENT REPLY ON|OFF|SKIP
```

**Available since:** 1.1.0
<!-- generated: end -->
Turns off the server's replies to this connection, to send a stream of commands without reading anything back.

- `OFF`: no replies, errors included, until `CLIENT REPLY ON`. `CLIENT REPLY OFF` gets no reply itself.
- `SKIP`: no reply to the next command alone, nor to `CLIENT REPLY SKIP` itself.
- `ON`: replies again, starting with `OK` to this command.

Pub/Sub messages and RESP3 push messages, such as client-side caching invalidations, are still sent. Without replies a client cannot tell whether a command failed, so this suits fire-and-forget writes, such as a bulk load whose result is checked afterwards.

## Reply

`OK` to `ON`; nothing to `OFF` or `SKIP`.

## Examples

```
> CLIENT REPLY SKIP
> SET a 1
> GET a
"1"
> CLIENT REPLY OFF
> SET a 2
> GET a
> CLIENT REPLY ON
OK
> GET a
"2"
```
