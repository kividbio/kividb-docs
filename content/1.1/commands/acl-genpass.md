---
title: "ACL GENPASS"
description: "Returns a random password, as hexadecimal digits, from the system's secure random source."
version: "1.1"
command: "ACL GENPASS"
syntax: "ACL GENPASS [bits]"
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
ACL GENPASS [bits]
```

**Available since:** 1.1.0
<!-- generated: end -->
Returns a random password, as hexadecimal digits, from the system's secure random source. `bits` is how much randomness, 256 by default, rounded up to a multiple of 4: each digit is 4 bits.

## Examples

```
> ACL GENPASS
"010d74e049c40b2e66cb9e3e8646c5bbba33d0f53eff04f45f80d2ef17534a5d"
> ACL GENPASS 32
"28de2381"
```
