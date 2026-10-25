---
title: "CLUSTER MIGRATION"
description: "Import the ranges from the node that owns them (one source per command)."
version: "1.2"
command: "CLUSTER MIGRATION"
syntax: "CLUSTER MIGRATION IMPORT start-slot end-slot [start-slot end-slot ...]"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
CLUSTER MIGRATION IMPORT start-slot end-slot [start-slot end-slot ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Import the ranges from the node that owns them (one source per command). Returns a task ID at once; the migration runs in the background.

The tasks this node knows of, as source or destination: `id`, `slots`, `source`, `dest`, `operation` (`import` / `migrate`), `state` (`in_progress`, `completed`, `failed`, `canceled`), `last_error`, `retries`, the three timestamps and `write_pause_ms`.

Cancel; returns the number of tasks cancelled. The source keeps the slots and the destination drops what it had received.
