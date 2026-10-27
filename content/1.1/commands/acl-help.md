---
title: "ACL HELP"
description: "In Redis, lists the ACL subcommands."
version: "1.1"
command: "ACL HELP"
syntax: "ACL HELP"
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
ACL HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
In Redis, lists the `ACL` subcommands.

## Known issue

KiviDB does not have `ACL HELP`: it replies `ERR unknown subcommand 'HELP'. Try ACL HELP.` Filed as [kividb#134](https://github.com/kividbio/kividb/issues/134), fixed in 1.2.
