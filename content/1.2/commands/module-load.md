---
title: "MODULE LOAD"
description: "Refused: KiviDB does not load modules, since Redis's module interface, a C library loaded into the server, does not fit KiviDB's design."
version: "1.2"
command: "MODULE LOAD"
syntax: "MODULE LOAD"
group: "other"
since: "1.1.0"
history: []
container: "MODULE"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
MODULE LOAD
```

**Available since:** 1.1.0
<!-- generated: end -->
Refused: KiviDB does not load modules, since Redis's module interface, a C library loaded into the server, does not fit KiviDB's design.

## Reply

- `ERR MODULE subsystem is not supported by KiviDB. ...`
