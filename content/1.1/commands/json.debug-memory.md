---
title: "JSON.DEBUG MEMORY"
description: "Returns the approximate size, in bytes, of each value path matches in the JSON document at key; of the whole document with no path."
version: "1.1"
command: "JSON.DEBUG MEMORY"
syntax: "JSON.DEBUG MEMORY key [path]"
group: "json"
since: "1.1.0"
history: []
container: "JSON.DEBUG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
JSON.DEBUG MEMORY key [path]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns the approximate size, in bytes, of each value `path` matches in the JSON document at `key`; of the whole document with no path.

## Examples

```
> JSON.DEBUG MEMORY d
(integer) 66
```
