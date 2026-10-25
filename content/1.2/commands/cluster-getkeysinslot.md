---
title: "CLUSTER GETKEYSINSLOT"
description: "Returns up to count of the keys this node holds in slot."
version: "1.2"
command: "CLUSTER GETKEYSINSLOT"
syntax: "CLUSTER GETKEYSINSLOT slot count"
group: "cluster"
since: "1.1.0"
history: []
container: "CLUSTER"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
CLUSTER GETKEYSINSLOT slot count
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns up to `count` of the keys this node holds in `slot`.

## Examples

```
> CLUSTER GETKEYSINSLOT 15495 10
1) "a"
2) "{a}1"
```
