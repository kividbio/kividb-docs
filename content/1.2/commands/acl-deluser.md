---
title: "ACL DELUSER"
description: "Deletes users."
version: "1.2"
command: "ACL DELUSER"
syntax: "ACL DELUSER username [username ...]"
group: "acl"
since: "1.1.0"
history: []
container: "ACL"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ACL DELUSER username [username ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Deletes users. The `default` user cannot be deleted.

## Reply

- The number of users deleted.
- `ERR The 'default' user cannot be removed`.

## Examples

```
> ACL DELUSER bob nobody
(integer) 1
> ACL DELUSER default
(error) ERR The 'default' user cannot be removed
```
