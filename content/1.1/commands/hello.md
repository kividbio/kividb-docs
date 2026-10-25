---
title: "HELLO"
description: "Switches the connection to RESP2 or RESP3, and returns the server's details: its name, version, protocol, connection ID, mode, role and modules, as a map under RESP3."
version: "1.1"
command: "HELLO"
syntax: "HELLO [protover [AUTH username password] [SETNAME clientname]]"
group: "server"
since: "1.1.0"
arity: -1
flags: ["fast"]
acl_categories: ["connection", "fast"]
history: []
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HELLO [protover [AUTH username password] [SETNAME clientname]]
```

**Available since:** 1.1.0 · **ACL categories:** `@connection`, `@fast`
<!-- generated: end -->
Switches the connection to RESP2 or RESP3, and returns the server's details: its name, version, protocol, connection ID, mode, role and modules, as a map under RESP3. `AUTH username password` logs in first, and `SETNAME name` names the connection.

## Reply

- The details.
- `ERR Protocol version is not an integer or out of range` for anything but 2 or 3.
- `NOAUTH`, without `AUTH`, when a password is required.

## Examples

```
> HELLO 3
1# "server" => "kividb"
2# "version" => "1.1.2"
3# "proto" => (integer) 3
4# "id" => (integer) 1
5# "mode" => "standalone"
6# "role" => "master"
7# "modules" => ...
```
