---
title: "HOTKEYS START"
description: "Start a session tracking the named metrics; COUNT is how many keys to report per metric, DURATION stops it automatically, SAMPLE tracks one command in ratio, SLOTS restricts it to those hash slots"
version: "1.1"
command: "HOTKEYS START"
syntax: "HOTKEYS START METRICS count [CPU] [NET] [COUNT k] [DURATION seconds] [SAMPLE ratio] [SLOTS count slot [slot ...]]"
group: "observability"
since: "1.1.0"
history: []
container: "HOTKEYS"
# generated: end
status: "draft"
---

<!-- generated: start -->
## Syntax

```
HOTKEYS START METRICS count [CPU] [NET] [COUNT k] [DURATION seconds] [SAMPLE ratio] [SLOTS count slot [slot ...]]
```

**Available since:** 1.1.0
<!-- generated: end -->
## Description

Start a session tracking the named metrics; `COUNT` is how many keys to report per metric, `DURATION` stops it automatically, `SAMPLE` tracks one command in `ratio`, `SLOTS` restricts it to those hash slots
