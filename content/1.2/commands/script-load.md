---
title: "SCRIPT LOAD"
description: "Compiles a script and caches it, without running it, and returns its SHA1 digest for EVALSHA."
version: "1.2"
command: "SCRIPT LOAD"
syntax: "SCRIPT LOAD script"
group: "scripting"
since: "1.1.0"
history: []
container: "SCRIPT"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
SCRIPT LOAD script
```

**Available since:** 1.1.0
<!-- generated: end -->
Compiles a script and caches it, without running it, and returns its SHA1 digest for [`EVALSHA`](evalsha.md).

## Examples

```
> SCRIPT LOAD "return ARGV[1]"
"098e0f0d1448c0a81dafe820f66d460eb09263da"
```
