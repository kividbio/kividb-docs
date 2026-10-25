---
title: "HIMPORT PREPARE"
description: "Define a named list of field names for this connection (Redis 8.10)."
version: "1.1"
command: "HIMPORT PREPARE"
syntax: "HIMPORT PREPARE fieldset field [field ...]"
group: "hash"
since: "1.1.0"
history: []
container: "HIMPORT"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HIMPORT PREPARE fieldset field [field ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Define a named list of field names for this connection (Redis 8.10). Fieldsets are private to the connection and go when it closes
