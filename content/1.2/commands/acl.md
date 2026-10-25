---
title: "ACL"
description: "Manages users and what each may do: which commands it may run, which keys it may read or write, which channels it may use."
version: "1.2"
command: "ACL"
syntax: "ACL"
group: "acl"
since: "1.1.0"
arity: -2
flags: ["admin"]
acl_categories: ["admin", "dangerous", "server", "slow"]
history: []
subcommands: ["ACL CAT", "ACL DELUSER", "ACL DRYRUN", "ACL GENPASS", "ACL GETUSER", "ACL HELP", "ACL LIST", "ACL LOAD", "ACL LOG", "ACL SAVE", "ACL SETUSER", "ACL USERS", "ACL WHOAMI"]
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
ACL
```

**Available since:** 1.1.0 · **ACL categories:** `@admin`, `@dangerous`, `@server`, `@slow`

Subcommands: [ACL CAT](acl-cat.md), [ACL DELUSER](acl-deluser.md), [ACL DRYRUN](acl-dryrun.md), [ACL GENPASS](acl-genpass.md), [ACL GETUSER](acl-getuser.md), [ACL HELP](acl-help.md), [ACL LIST](acl-list.md), [ACL LOAD](acl-load.md), [ACL LOG](acl-log.md), [ACL SAVE](acl-save.md), [ACL SETUSER](acl-setuser.md), [ACL USERS](acl-users.md), [ACL WHOAMI](acl-whoami.md)
<!-- generated: end -->
Manages users and what each may do: which commands it may run, which keys it may read or write, which channels it may use. The `default` user always exists; new connections are logged in as it. See its subcommands, and [`AUTH`](auth.md).
