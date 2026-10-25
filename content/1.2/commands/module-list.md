---
title: "MODULE LIST"
description: "Names the built-in families clients look for, with the versions of Redis 8.10's, and an empty path, as Redis lists its built-in vectorset: search, ReJSON, timeseries and vectorset."
version: "1.2"
command: "MODULE LIST"
syntax: "MODULE LIST"
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
MODULE LIST
```

**Available since:** 1.1.0
<!-- generated: end -->
Names the built-in families clients look for, with the versions of Redis 8.10's, and an empty path, as Redis lists its built-in `vectorset`: `search`, `ReJSON`, `timeseries` and `vectorset`.

## Examples

```
> MODULE LIST
1) 1) "name"
   2) "search"
   3) "ver"
   4) (integer) 81001
   5) "path"
   6) ""
   7) "args"
   8) (empty array)
...
```
