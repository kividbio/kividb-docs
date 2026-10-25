---
title: "FT.CONFIG GET"
description: "The query engine's settings by RediSearch's names (TIMEOUT, DEFAULT_DIALECT, MINPREFIX, MAXSEARCHRESULTS, CURSOR_MAX_IDLE, …), as [name, value] pairs; * for all"
version: "1.2"
command: "FT.CONFIG GET"
syntax: "FT.CONFIG GET option|pattern"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG GET option|pattern
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

The query engine's settings by RediSearch's names (`TIMEOUT`, `DEFAULT_DIALECT`, `MINPREFIX`, `MAXSEARCHRESULTS`, `CURSOR_MAX_IDLE`, …), as `[name, value]` pairs; `*` for all
