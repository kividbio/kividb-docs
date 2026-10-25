---
title: "ACL DRYRUN"
description: "Tells whether a user could run a command, without running it."
version: "1.1"
command: "ACL DRYRUN"
syntax: "ACL DRYRUN username command [arg ...]"
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
ACL DRYRUN username command [arg ...]
```

**Available since:** 1.1.0
<!-- generated: end -->
Tells whether a user could run a command, without running it.

## Reply

- `OK` if it could.
- A description of why not, as a bulk string.

## Examples

```
> ACL DRYRUN alice GET cache:1
OK
> ACL DRYRUN alice GET other
"User alice has no permissions to access the 'other' key"
> ACL DRYRUN alice DEL cache:1
"User alice has no permissions to run the 'del' command"
```
