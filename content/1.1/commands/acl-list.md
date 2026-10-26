---
title: "ACL LIST"
description: "Returns every user as a line of the ACL file format: user <name> <on|off> <passwords> <key patterns> <channel patterns> <command rules>."
version: "1.1"
command: "ACL LIST"
syntax: "ACL LIST"
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
ACL LIST
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns every user as a line of the ACL file format: `user <name> <on|off> <passwords> <key patterns> <channel patterns> <command rules>`.

## Examples

```
> ACL LIST
1) "user alice on #1ec1c26b... ~cache:* &news -@all +get +set"
2) "user bob on #30c952fa... %R~* resetchannels -@all +@read"
3) "user default on nopass ~* &* +@all"
```
