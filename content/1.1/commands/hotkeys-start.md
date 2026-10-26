---
title: "HOTKEYS START"
description: "Starts a session that tracks, per key, the metrics named: CPU (CPU time) and NET (network bytes)."
version: "1.1"
command: "HOTKEYS START"
syntax: "HOTKEYS START METRICS count [CPU] [NET] [COUNT k] [DURATION seconds] [SAMPLE ratio] [SLOTS count slot [slot ...]]"
group: "observability"
since: "1.1.0"
history: []
container: "HOTKEYS"
# generated: end
status: "reviewed"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS START METRICS count [CPU] [NET] [COUNT k] [DURATION seconds] [SAMPLE ratio] [SLOTS count slot [slot ...]]
```

**Available since:** 1.1.0
<!-- generated: end -->
Starts a session that tracks, per key, the metrics named: `CPU` (CPU time) and `NET` (network bytes). `METRICS count` is how many metrics follow.

## Options

| Option | Effect |
|---|---|
| `COUNT k` | How many keys to report per metric. |
| `DURATION seconds` | Stop the session by itself after this long. |
| `SAMPLE ratio` | Track one command in `ratio`, to cost less. |
| `SLOTS count slot ...` | Track only keys in these hash slots. |

## Examples

```
> HOTKEYS START METRICS 2 CPU NET COUNT 3
OK
```
