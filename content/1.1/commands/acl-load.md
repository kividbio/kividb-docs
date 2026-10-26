---
title: "ACL LOAD"
description: "Replaces every user with those in the ACL file, the aclfile setting."
version: "1.1"
command: "ACL LOAD"
syntax: "ACL LOAD"
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
ACL LOAD
```

**Available since:** 1.1.0
<!-- generated: end -->
Replaces every user with those in the ACL file, the `aclfile` setting.

## Reply

- `OK`.
- An error if no ACL file is configured, or the file is not valid; then nothing changes.
