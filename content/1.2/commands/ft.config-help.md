---
title: "FT.CONFIG HELP"
description: "Lists the FT.CONFIG subcommands and what each does."
version: "1.2"
command: "FT.CONFIG HELP"
syntax: "FT.CONFIG HELP"
group: "vector-search"
since: "1.1.0"
history: []
container: "FT.CONFIG"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
FT.CONFIG HELP
```

**Available since:** 1.1.0
<!-- generated: end -->
Lists the search settings that [`FT.CONFIG GET`](ft.config-get.md) and [`FT.CONFIG SET`](ft.config-set.md) know, each with its current value. With a name or glob-style pattern, matched without regard to case, it lists only the settings that match, and an empty array if none do.

Each entry is the setting's name, then `Description` and an empty string, then `Value` and the value. The description is always empty: [`FT.CONFIG`](ft.config.md) and [`FT.CONFIG SET`](ft.config-set.md) say which settings are acted on and what they do.

## Reply

An array with an entry for each setting, 23 in all.

## Examples

```
> FT.CONFIG HELP
 1) 1) "CURSOR_MAX_IDLE"
    2) "Description"
    3) ""
    4) "Value"
    5) "300000"
 2) 1) "TIMEOUT"
    2) "Description"
    3) ""
    4) "Value"
    5) "0"
...
23) 1) "BM25STD_TANH_FACTOR"
    2) "Description"
    3) ""
    4) "Value"
    5) "4"
> FT.CONFIG HELP *timeout
1) 1) "TIMEOUT"
   2) "Description"
   3) ""
   4) "Value"
   5) "0"
2) 1) "ON_TIMEOUT"
   2) "Description"
   3) ""
   4) "Value"
   5) "return"
```
