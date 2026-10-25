---
title: "XGROUP CREATE"
description: "Create a consumer group; $ starts from the latest entry; MKSTREAM creates the key if absent"
version: "1.1"
command: "XGROUP CREATE"
syntax: "XGROUP CREATE key group id|$ [MKSTREAM] [ENTRIESREAD n]"
group: "stream"
since: "1.1.0"
history: []
container: "XGROUP"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
XGROUP CREATE key group id|$ [MKSTREAM] [ENTRIESREAD n]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Create a consumer group; `$` starts from the latest entry; MKSTREAM creates the key if absent
