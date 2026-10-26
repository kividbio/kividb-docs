---
title: "ACL GETUSER"
description: "Returns a user's rules: its flags, the SHA-256 hashes of its passwords, its command rules, its key and channel patterns, and its selectors."
version: "1.2"
command: "ACL GETUSER"
syntax: "ACL GETUSER username"
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
ACL GETUSER username
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns a user's rules: its flags, the SHA-256 hashes of its passwords, its command rules, its key and channel patterns, and its selectors.

## Reply

- A flat array of names and values.
- `nil` if there is no such user.

## Examples

```
> ACL GETUSER alice
 1) "flags"
 2) 1) "on"
 3) "passwords"
 4) 1) "1ec1c26b50d5d3c58d9583181af8076655fe00756bf7285940ba3670f99fcba0"
 5) "commands"
 6) "-@all +get +set"
 7) "keys"
 8) "~cache:*"
 9) "channels"
10) "&news"
11) "selectors"
12) (empty array)
```
