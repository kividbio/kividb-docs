---
title: "SCRIPT EXISTS"
description: "Tells, for each SHA1 digest, whether the script is cached."
version: "1.1"
command: "SCRIPT EXISTS"
syntax: "SCRIPT EXISTS sha1 [sha1 ...]"
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
SCRIPT EXISTS sha1 [sha1 ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Tells, for each SHA1 digest, whether the script is cached.

## Reply

- An array with `1` or `0` for each digest.

## Examples

```
> SCRIPT EXISTS 098e0f0d1448c0a81dafe820f66d460eb09263da ffffffffffffffffffffffffffffffffffffffff
1) (integer) 1
2) (integer) 0
```
