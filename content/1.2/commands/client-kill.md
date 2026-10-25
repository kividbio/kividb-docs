---
title: "CLIENT KILL"
description: "Close the matching connections."
version: "1.2"
command: "CLIENT KILL"
syntax: "CLIENT KILL ip:port | CLIENT KILL [ID id] [TYPE type] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]"
group: "server"
since: "1.1.0"
history: []
container: "CLIENT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLIENT KILL ip:port | CLIENT KILL [ID id] [TYPE type] [USER username] [ADDR ip:port] [LADDR ip:port] [SKIPME yes|no] [MAXAGE seconds]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Close the matching connections. The old form (`ip:port`) replies `OK` or `ERR No such client`; the filter form replies with the number killed. `SKIPME` defaults to `yes`; with `no` the caller is killed too, after it has been sent the reply. Killed connections get no reply
