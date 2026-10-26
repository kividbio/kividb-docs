---
title: "FUNCTION LOAD"
description: "Loads a library of functions."
version: "1.2"
command: "FUNCTION LOAD"
syntax: "FUNCTION LOAD [REPLACE] library-code"
group: "scripting"
since: "1.1.0"
history: []
container: "FUNCTION"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FUNCTION LOAD [REPLACE] library-code
```

**Available since:** 1.1.0
<!-- generated: end -->
Loads a library of functions. Its first line names it, `#!lua name=<library>`, and its code registers functions with `redis.register_function`.

```lua
#!lua name=mylib
redis.register_function('hello', function(keys, args) return 'hi ' .. args[1] end)
redis.register_function{
  function_name = 'getk',
  callback = function(keys) return redis.call('GET', keys[1]) end,
  flags = {'no-writes'},
  description = 'read a key',
}
```

While a library loads, only `redis.register_function`, `redis.log` and the version constants are in reach: no `redis.call`, no `math`. It cannot set globals, and it is stopped after 500 ms. A load is all of a library or none of it: an error leaves the library it was to replace as it was. A function name belongs to one library. Library names are case-sensitive. A load is refused at the memory limit.

## Options

- `REPLACE`: replace a library of that name.

## Reply

- The library's name.
- `ERR Library 'mylib' already exists. Use REPLACE to overwrite it.`
- `ERR Missing library metadata` without the `#!lua name=` line.

## Examples

```
> FUNCTION LOAD "#!lua name=mylib\n..."
"mylib"
> FCALL hello 0 Ada
"hi Ada"
```
